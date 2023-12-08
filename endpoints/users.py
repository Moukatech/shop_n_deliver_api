from utilities.request_utilities import RequestUtilities
# from assertpy import assert_that

request_utilities = RequestUtilities()

def create_user_endpoint(data):
    response=request_utilities.post("api/users", payload=data)
    return response

def update_user_endpoint(data,id):
    response=request_utilities.update(f"api/users/{id}", payload=data)
    return response

def delete_user_endpoint(id):
    response=request_utilities.delete(f"api/users/{id}")
    return response