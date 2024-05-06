import gen.openapi_client as openapi_client
from openapi_client.api import default_api

if __name__ == '__main__':
    configuration = openapi_client.Configuration(host="http://localhost:8000")

    with openapi_client.ApiClient(configuration) as api_client:

        api_instance = default_api.DefaultApi(api_client)

        try:
            user_id_1 = api_instance.users_post(payload={"name": "test", "login": "test", "password": "test"})
            print(user_id_1)

            user_id_2 = api_instance.users_post(payload={"name": "test2", "login": "test2", "password": "test2"})
            print(user_id_2)

            api_response = api_instance.users_get()
            print(api_response)

            api_instance.users_user_id_delete(user_id=user_id_1["user_id"])

            api_response = api_instance.users_get()
            print(api_response)

        except openapi_client.ApiException as e:
            print(e)
