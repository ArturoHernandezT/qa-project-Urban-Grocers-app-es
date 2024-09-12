import requests
import configuration as c
import data as d

# CREACIÓN DE USUARIO
def post_new_user(body):
    return requests.post(c.URL_SERVICE + c.CREATE_USER_PATH,
                         json=body,
                         headers=d.headers_user)

"""response = post_new_user(d.user_body) 
auth_token = response.json()["authToken"] # VARIABLE QUE ALMACENA EL AUTHTOKEN
print(response.json()["authToken"])
print(response.status_code)"""


# CREACIÍON DE NUEVO KIT
def post_new_client_kit(kit_body):
    return requests.post(c.URL_SERVICE + c.KITS_PATH, json=d.kit_data, headers=d.headers_kit)


# CREACIÓN DE NUEVO KIT SIN PARAMETRO "NAME"
def post_new_client_kit_whithout_name(kit_body):
    return requests.post(c.URL_SERVICE + c.KITS_PATH, json=d.kit_data_sin_parametro_name, headers=d.headers_kit)
