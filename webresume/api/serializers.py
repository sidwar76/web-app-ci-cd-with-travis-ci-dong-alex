from rest_framework_json_api import serializers
from .models import Person

# API endpoint that allows persons to be viewed or edited
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name','contact', 'about', 'education', 'skills', 'work')

    
