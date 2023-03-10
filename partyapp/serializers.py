from rest_framework.serializers import ModelSerializer
from .models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel

class PoliticalPartySerializer(ModelSerializer):
    class Meta:
        model=PoliticalPartyModel
        fields='__all__'

class PoliticalLeaderSerializer(ModelSerializer):
    class Meta:
        model=PoliticalLeaderModel
        fields='__all__'

class DevelopmentSerializer(ModelSerializer):
    class Meta:
        model=DevelopmentModel
        fields='__all__'
