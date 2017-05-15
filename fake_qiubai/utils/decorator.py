# encoding: utf-8
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from functools import wraps
from rest_framework.response import Response

def auth_required(cls):
    cls.authentication_classes = (SessionAuthentication, TokenAuthentication)
    # cls.permission_classes = (IsAuthenticated,)
    return cls

def xlogin_required(func):
    @wraps(func)
    def wrapper(api_view, request):
        if not request.user.is_authenticated:
            return Response({'status':9, 'error_msg':'Login Required'})
        result = func(api_view, request)
        return result

    return wrapper
