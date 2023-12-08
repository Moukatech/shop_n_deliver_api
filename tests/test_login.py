from endpoints.login import login_endpoint


def test_valid_login():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    rs_data=login_endpoint(data)
    rs_json= rs_data.json()
    assert rs_data.status_code==200
    assert rs_json["token"] is not None
    
    
    
def test_invalid_login_missing_password():
    data = {
    "email": "eve.holt@reqres.in",
    }
    rs_data=login_endpoint(data)
    rs_json= rs_data.json()
    assert rs_data.status_code==400
    assert rs_json["error"] == "Missing password"