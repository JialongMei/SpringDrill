from rest_framework import serializers
from .models import Character, CombatEngraving, AllClass
from django.contrib.auth.models import User


class AllClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllClass
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    the_class = serializers.PrimaryKeyRelatedField(queryset=AllClass.objects.all())

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        class_name = validated_data.pop('the_class')
        current_user = self.context['request'].user

        character = Character.objects.create(the_class=class_name, owner=current_user, **validated_data)

        return character

class CombatEngravingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CombatEngraving
        fields = ['name', 'description']
