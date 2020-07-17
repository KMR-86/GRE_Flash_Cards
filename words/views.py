from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from words.models import words
from words.serializers import WordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class word_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """

    def get(self, request):
        if request.method == 'GET':
            all_words = words.objects.all()
            serializer = WordSerializer(all_words, many=True)
            return Response(serializer.data)  # this one is for fancy rest framework response
            # return JsonResponse(serializer.data, safe=False) #this one will only give the json format

    def post(self, request, format=None):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WordDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return words.objects.get(pk=pk)
        except words.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)