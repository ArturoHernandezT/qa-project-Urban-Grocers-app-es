import data as d
import sender_stand_request


# FUNCION  PARA CREAR UNA COPIA
def get_kit_body(kit_name):
    current_body = d.kit_data.copy()
    current_body["name"] = kit_name
    return current_body


# PRUEBAS POSITIVAS
def positive_assert(name):
    kit_body = get_kit_body(name)  # Esta linea deberia realizar la copia de la prueba
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    print(f"Status code: {kit_response.status_code}")  # linea para saber cual es el codigo que se esta generando
    assert kit_response.status_code == 201
    return kit_response


def test_create_kit_1_character():
    positive_assert("a")


def test_create_kit_511_characteres():
    positive_assert(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\\"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\\"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\\"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\\"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test_create_kit_special_characteres():
    positive_assert("№%@,")


def test_create_kit_space():
    positive_assert(" A Aaa")


def test_create_kit_str_number():
    positive_assert("123")


# PRUEBAS NEGATIVAS
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    print(f"Status code: {kit_response.status_code}")
    assert kit_response.status_code == 400
    return kit_response


def test_create_kit_empty_characteres():
    negative_assert_code_400("")


def test_create_kit_512_characteres():
    negative_assert_code_400(
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\\"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\\"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\\"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\\"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test_create_kit_number():
    negative_assert_code_400(123)


# PRUEBA NEGATIVA SIN PARAMETROS

def negative_assert_code_400_whithout_parameter(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    print(f"Status code: {kit_response.status_code}")
    assert kit_response.status_code == 400
    return kit_response


def test_create_kit_without_parameter_name():
    negative_assert_code_400_whithout_parameter("")
