from rest_framework import serializers
from words.models import words


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = words
        fields = '__all__'

