from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from functools import wraps
from rest_framework.parsers import JSONParser
from utils.joi import joi

def validate_body_request(validationobject:joi):
    def main(fn):
        def wrap(self,request, *args, **kwargs):
            try:
                # Parse the request body as JSON
                request_data = JSONParser().parse(request)
                validation_result = validationobject.validate(request_data)

                if not validation_result['accepted']:
                    return JsonResponse({
                        "missing_fields":validation_result['missing_fields'],
                        "wrong_field":validation_result['wrong_field']
                    },status=status.HTTP_400_BAD_REQUEST,safe=False)
                
                
                return fn(self,request, *args, **kwargs)
            except Exception as e:
                return JsonResponse(str(e), status=400, safe=False)

        return wrap

    return main