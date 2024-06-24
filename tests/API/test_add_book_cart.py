import allure
from jsonschema.validators import validate

from litres_shop.schema.put_no_book_to_cart import add_non_existent_book
from litres_shop.schema.put_book_cart import book_cart
from litres_shop.utils.api_request import litres_api_put


@allure.epic('Cart API')
@allure.feature("Add cart")
@allure.label('api')
@allure.tag('regress', 'api', 'cart')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_add_book_to_cart():
    art_ids = [6375365]
    url = f"/foundation/api/cart/arts/add"
    response = litres_api_put(url, json={"art_ids": art_ids})

    assert response.status_code == 200
    validate(response.json(), book_cart)
    assert response.json()['payload']['data']['added_art_ids'] == art_ids
    assert response.json()['payload']['data']['failed_art_ids'] == []


# pass
@allure.epic('Cart API')
@allure.feature("No book cart")
@allure.label('api')
@allure.tag('regress', 'api', 'cart')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_add_no_existent_book_to_cart():
    art_ids = ["null"]
    url = f"/foundation/api/cart/arts/add"
    response = litres_api_put(url, json={"art_ids": art_ids})

    assert response.status_code == 422
    validate(response.json(), add_non_existent_book)
# pass

