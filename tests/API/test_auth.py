import os

import allure
from dotenv import load_dotenv
from jsonschema.validators import validate

from litres_shop.schema.post_auth_user import auth_user
from litres_shop.utils.api_request import litres_api_post


@allure.epic('Auth API')
@allure.feature("Auth user")
@allure.label('api')
@allure.tag('regress', 'api', 'auth')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_auth():
    load_dotenv()
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    url = f"/foundation/api/auth/login"

    response = litres_api_post(url, json={"login": email, "password": password})

    assert response.status_code == 200
    validate(response.json(), auth_user)
    assert response.json()['error'] is None
# pass
