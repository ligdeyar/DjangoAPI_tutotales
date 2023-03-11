from rest_framework import serializers 
from DjangoAPI.models import Django
 
 
class DjangoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Django
        fields = ('id',
                  'title',
                  'description',
                  'published')
