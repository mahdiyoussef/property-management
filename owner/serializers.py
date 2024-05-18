from owner.models import manager,owner
from rest_framework import serializers



class ManagerSerializer(serializers.ModelSerializer):
    class meta:
        model = manager
        fields = '__all__'



class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = ['id', 'firstname', 'lastname', 'nationalid', 'passportnumber', 'addressline1', 'addressline2', 'city', 'country', 'managerid', 'active']
        extra_kwargs = {
            'managerid': {'required': False},
            'nationalid': {'required': False},
            'passportnumber': {'required': False},
            'active': {'required': False}
        }
