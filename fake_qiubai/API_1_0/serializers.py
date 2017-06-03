# encoding: utf-8
from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeUser
        fields = ('nickname',)