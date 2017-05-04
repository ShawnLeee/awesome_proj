# encoding: utf-8
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','content')