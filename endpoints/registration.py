from utilities.request_utilities import RequestUtilities
# from assertpy import assert_that

request_utilities = RequestUtilities()

def register_endpoint(data):
    response=request_utilities.post("api/register", payload=data)
    return response