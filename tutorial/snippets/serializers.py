from rest_framework import serializers
from .models import Snippet, STYLE_CHOICES, LANGUAGE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style')
    