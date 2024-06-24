import allure
from jsonschema.validators import validate

from litres_shop.schema.get_search_audiobook import search_audiobook
from litres_shop.schema.get_search_no_results import serach_no_results
from litres_shop.utils.api_request import litres_api_get


@allure.epic('Search API')
@allure.feature("Search audiobook")
@allure.label('api')
@allure.tag('regress', 'api', 'search')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_search_audiobook():
    book_title = 'Под Куполом'
    art_types = 'audiobook'
    types = 'audiobook'
    url = f"/foundation/api/search?q={book_title}&art_types={art_types}&types={types}"
    response = litres_api_get(url)
    body = response.json()

    assert response.status_code == 200
    validate(body, search_audiobook)
    assert body['payload']['data'][0]['type'] == "audiobook"
    assert body['payload']['data'][0]['instance']['title'] == 'Под Куполом'


# pass

@allure.epic('Search API')
@allure.feature("Search no results")
@allure.label('api')
@allure.tag('regress', 'api', 'search')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_search_no_results():
    book_title = 'такойкнигинет'
    art_types = 'audiobook'
    types = 'audiobook'
    url = f"/foundation/api/search?q={book_title}&art_types={art_types}&types={types}"
    response = litres_api_get(url)
    body = response.json()

    assert response.status_code == 200
    validate(body, serach_no_results)
    assert len(response.json()['payload']['data']) == 0
# pass
