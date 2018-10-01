from rest_framework_json_api import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name','contact', 'about', 'education', 'skills', 'work')

    
