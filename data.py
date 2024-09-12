
# CREACIÓN DE USUARIO

headers_user = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Arturo H",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

# CREACIÓN DE KIT

headers_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ca3e3124-f77f-4e27-904f-f7e12b51a586"
}

# DATOS DEL KIT
kit_data = {
    "cardId": 102,
    "name": "Kit de Prueba No.2 "
}

# DATOS DEL IDS
headers_ids = {
    "Content-Type": "application/json"
}
product_ids = {
    "ids": [1, 2, 3]
}

# DATOS DEL KIT SIN PARAMETRO "NAME"

kit_data_sin_parametro_name = {
    "cardId": 102
}
