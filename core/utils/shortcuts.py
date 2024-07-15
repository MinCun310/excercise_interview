from rest_framework.response import Response
from rest_framework import status


def standard_response(data=None, message="", response_type="success", http_status_code=status.HTTP_200_OK):
    return Response({
        "status": response_type,
        "http_status_code": http_status_code,
        "message": message,
        "data": data
    }, status=http_status_code)


def success_response(data=None, message="Success", http_status_code=status.HTTP_200_OK):
    return standard_response(data, message, response_type="success", http_status_code=http_status_code)


def error_response(data=None, message="Error", http_status_code=status.HTTP_400_BAD_REQUEST, feature_code=None):
    response = standard_response(data, message, response_type="error", http_status_code=http_status_code)
    if feature_code:
        response.data["error_feature_code"] = feature_code
    return response
