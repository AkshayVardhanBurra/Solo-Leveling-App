

from rest_framework.serializers import ModelSerializer
from models import UserData, Task

class UserDataSerializer(ModelSerializer):

    class Meta:
        model = UserData
        fields = ("curr_xp", "next_xp", "level", "date_created")
        
