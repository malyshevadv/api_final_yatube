from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def ValidationError400(exc, context):
    response = exception_handler(exc, context)
    if response is None and isinstance(exc, ValidationError):
        return Response(exc, status=400)

    return response
