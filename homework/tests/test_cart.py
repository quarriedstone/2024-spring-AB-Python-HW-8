import json


def test_get_cart_by_id(cart_api):
    create_cart_response = cart_api.create_cart_cart_post()
    cart_data = json.loads(create_cart_response.response.data.decode('utf-8'))
    cart_id = cart_data["id"]

    get_cart_response = cart_api.get_cart_by_id_cart_cart_id_get(path_params={"cart_id": cart_id})
    retrieved_cart_data = json.loads(get_cart_response.response.data.decode('utf-8'))

    assert retrieved_cart_data["id"] == cart_id
    assert retrieved_cart_data["products"] == []


def test_create_cart(cart_api):
    response = cart_api.create_cart_cart_post()
    cart_data = json.loads(response.response.data.decode('utf-8'))

    assert "id" in cart_data
    assert "products" in cart_data
    assert isinstance(cart_data["products"], list)
    assert cart_data["products"] == []


def test_add_to_cart(cart_api, products_api):
    create_cart_response = cart_api.create_cart_cart_post()
    cart_data = json.loads(create_cart_response.response.data.decode('utf-8'))
    cart_id = cart_data["id"]

    product_data = {"name": "Eggs", "price": 100.5}
    products_api.create_product_products_post(body=product_data)

    add_to_cart_response = cart_api.add_to_cart_cart_cart_id_put(
        path_params={"cart_id": cart_id},
        query_params={"product_name": "Eggs", "quantity": 12},
    )
    assert add_to_cart_response.response.status == 200

    get_cart_response = cart_api.get_cart_by_id_cart_cart_id_get(path_params={"cart_id": cart_id})
    updated_cart_data = json.loads(get_cart_response.response.data.decode('utf-8'))

    product_found = any(item["product"]["name"] == 'Eggs' and item["quantity"] == 12 for item in updated_cart_data["products"])
    assert product_found
