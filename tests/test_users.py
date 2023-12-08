from endpoints.users import create_user_endpoint, update_user_endpoint, delete_user_endpoint


def test_verify_successful_user():
    data = {
    "name": "morpheus",
    "job": "leader"
}
    rs_data=create_user_endpoint(data)
    rs_json= rs_data.json()
    print(rs_json)
    assert rs_data.status_code==201
    assert rs_json["name"] == "morpheus"
    assert rs_json["job"] == "leader"
    
def test_verify_failed_user_creation():
    data = {
    "name": "john",
    "job": "leader"
    
}
    rs_data=create_user_endpoint(data)
    rs_json= rs_data.json()
    print(rs_json)
    assert rs_data.status_code==201
    

def test_verify_successful_user_update():
    data = {
    "name": "morpheus",
    "job": "zion resident"
}
    rs_data=update_user_endpoint(data, 50)
    rs_json= rs_data.json()
    print(rs_json)
    assert rs_data.status_code==200
    assert rs_json["name"] == "morpheus"
    assert rs_json["job"] == "zion resident"

def test_verify_successful_delete_user():

    rs_data=delete_user_endpoint(1)
    assert rs_data.status_code==204