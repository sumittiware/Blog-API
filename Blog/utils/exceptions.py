from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc,context):

    handlers={
        'ValidationError':{
            'status':status.HTTP_400_BAD_REQUEST,
            'error':'Please make a request with proper data'
        },
        'Http404': {
            'status':status.HTTP_400_BAD_REQUEST,
            'error':"Resourse not found"
        },
        'PermissionDenied': {
            'status':status.HTTP_401_UNAUTHORIZED,
            'error':"You are not authorised to perform this action"
        },
        'NotAuthenticated': {
            'status': status.HTTP_401_UNAUTHORIZED,
            'error':'Please, make sure you are logged In'
        }
    }

    response = exception_handler(exc,context)

    exception_class=exc.__class__.__name__

    if exception_class in handlers:
        response.data = handlers[exception_class]
        return response
    return response

