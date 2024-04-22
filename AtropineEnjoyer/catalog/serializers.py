from rest_framework import serializers
from .models import Character,CombatEngraving


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    # class_name = serializers.RelatedField(source='the_class.name', read_only=True).to_representation
    # owner_name = serializers.RelatedField(source='owner.username', read_only=True).to_representation

    class Meta:
        model = Character

    def to_representation(self, instance):
        representation = dict()
        representation['name'] = instance.name
        representation['the_class'] = instance.the_class.name
        representation['ilv'] = instance.ilv
        representation['owner'] = instance.owner.username

        return representation


class CombatEngravingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CombatEngraving
        fields = ['name', 'description']
