from drf_yasg import openapi

from loan_manager.common import field_names


# post = 'post'
# get = 'get'
# put = 'put'
# delete = 'delete'

post_ = 'POST'
get_ = 'GET'
put_ = 'PUT'
delete_ = 'DELETE'

# param names to endpoint to be used in swagger
type_string = openapi.Schema(type=openapi.TYPE_STRING)
type_integer = openapi.Schema(type=openapi.TYPE_INTEGER)
type_object = openapi.TYPE_OBJECT

subscription_req_desc = 'subscription to borrower or manager to operating on api'
subscription_req_body = openapi.Schema(
    type=type_object,
    required=[field_names.name, field_names.email, field_names.type],
    properties={
        field_names.name: type_string,
        field_names.email: type_string,
        field_names.type: type_string
    },
)

subscription_list_desc = 'get details of all subscribers'
# name = openapi.Parameter('name', in_=openapi.IN_QUERY, description='customer name', type=openapi.TYPE_STRING)
# email = openapi.Parameter('email', in_=openapi.IN_BODY, description='customer subscription email', type=openapi.TYPE_STRING)

new_jwt_req_desc = 'get new jwt token acting as refreshing token whose expiry needs to be checked'
new_jwt_req_body = openapi.Schema(
    type=type_object,
    required=[field_names.user],
    properties={
        field_names.user: type_string,
    },
)
