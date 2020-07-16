from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from words.models import words
from words.serializers import WordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class word_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self,request):
        if request.method == 'GET':
            all_words = words.objects.all()
            serializer = WordSerializer(all_words, many=True)
            #return Response(serializer.data)  #this one is for fancy rest framework response
            return JsonResponse(serializer.data, safe=False)
