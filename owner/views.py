from rest_framework.views import APIView
from owner.models import manager,owner
from owner.serializers import OwnerSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from utils.validatebody import validate_body_request
from owner.forms import create_owner



class OwnerView(APIView):
    
    
    def get(self,request):
        try:
            print(request.GET.dict())
            all_owners = owner.objects.all()
            all_owners_serializer = OwnerSerializer(all_owners,many=True)
            return JsonResponse(all_owners_serializer.data,safe=False,status=200)
        
        except Exception as e:
            return JsonResponse("failed to get",safe=False,status=400)
    

    @validate_body_request(create_owner)
    def post(self, request):
        try:
            owner_data = JSONParser().parse(request)
            print(owner_data)
            owner_serialized = OwnerSerializer(data=owner_data)
            if owner_serialized.is_valid():
                print("is valid")
                owner_serialized.save()
                return JsonResponse(owner_serialized.data, status=201,safe=False)
            else:
                return JsonResponse(owner_serialized.errors, status=400,safe=False)
        except Exception as e:
            return JsonResponse(str(e), status=500,safe=False)
