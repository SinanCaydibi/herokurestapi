from rest_framework import serializers

from api.models import Data
class OksiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = '__all__'
        
class OksiUpdateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = [
            'oksi'
        ]


