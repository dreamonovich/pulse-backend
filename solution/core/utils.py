from rest_framework.response import Response
from rest_framework.views import exception_handler
from core.exceptions import ReasonException

def custom_exception_handler(exc, context):
    if isinstance(exc, ReasonException):
        return Response({'reason': exc.reason}, status=exc.status_code)
    else:
        exception_handler()