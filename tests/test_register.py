from endpoints.registration import register_endpoint


def test_verify_valid_user_registration():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    rs_data=register_endpoint(data)
    rs_json= rs_data.json()
    print(rs_json)
    assert rs_data.status_code==200
    assert rs_json["token"] is not None

def test_verify_invalid_user_registration():
    data = {
    "email": "eve.holt@reqres.in",

    }
    rs_data=register_endpoint(data)
    rs_json= rs_data.json()
    print(rs_json)
    assert rs_data.status_code==400
    assert rs_json["error"] == "Missing password"
    
    