from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def DjangoAPI_list(request):
    # GET list , POST a new , DELETE all 
    def DjangoAPI_list(request):
    if request.method == 'GET':
        DjangoAPI = DjangoAPI.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            DjangoAPI = DjangoAPI.filter(title__icontains=title)
        
        DJangoSerializer(DjangoAPI, many=True)
        return JsonResponse(DjangoAPI_serializer.data, safe=False)
    
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def DjangoAPI_detail(request, pk):
    try: 
        DjangoAPI = DjangoAPI.objects.get(pk=pk) 
    except DjangoAPI.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE 
    
        
@api_view(['GET'])
def DjangoAPI_list_published(request):
    # GET all published 