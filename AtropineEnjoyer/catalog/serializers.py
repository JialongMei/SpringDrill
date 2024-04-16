from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class_name = serializers.CharField(source='the_class.name')

    class Meta:
        model = Character
        fields = ['name', 'class_name']

