from utilities.request_utilities import RequestUtilities
# from assertpy import assert_that

request_utilities = RequestUtilities()

def login_endpoint(data):
    response=request_utilities.post("api/login", payload=data)
    return response