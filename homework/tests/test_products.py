import json


def test_create_product(products_api):
    product_data = {"name": "Cake", "price": 10.0}
    response = products_api.create_product_products_post(body=product_data)
    product = json.loads(response.response.data.decode('utf-8'))

    assert "id" in product
    assert product["name"] == "Cake"
    assert product["price"] == 10.0


def test_get_products(products_api):
    response = products_api.get_products_products_get()
    products = json.loads(response.response.data.decode('utf-8'))

    assert isinstance(products, list)


def test_update_product(products_api):
    product_data = {"name": "Biscuit", "price": 20.0}
    create_response = products_api.create_product_products_post(body=product_data)
    created_product = json.loads(create_response.response.data.decode('utf-8'))
    product_id = created_product["id"]

    updated_product_data = {"name": "Cookie", "price": 25.0}
    update_response = products_api.update_product_info_products_product_id_put(
        path_params={"product_id": product_id},
        body=updated_product_data
    )
    updated_product = json.loads(update_response.response.data.decode('utf-8'))

    assert updated_product["id"] == product_id
    assert updated_product["name"] == "Cookie"
    assert updated_product["price"] == 25.0
