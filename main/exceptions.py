from rest_framework.exceptions import APIException
from rest_framework import status


class MadlibServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'Looks like Madlib is unavailable at the moment. Try again later!'
    default_code = 'service_unavailable'
