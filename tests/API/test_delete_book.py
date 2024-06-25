import allure

from litres_shop.utils.api_request import litres_api_delete


@allure.epic('Wishlist API')
@allure.feature("Delete book at wishlist")
@allure.label('api')
@allure.tag('regress', 'api', 'search')
@allure.severity('normal')
@allure.label("owner", "polushina")
def test_delete_book_at_wishlist():
    headers = {
        'wishlist': '4387285'
    }
    url = f"/foundation/api/wishlist/arts/4387285"
    response = litres_api_delete(url, headers=headers)
    assert response.status_code == 204
# pass
