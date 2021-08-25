from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class DoctorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorType
        fields = '__all__'

    def to_representation(self, value):
        return value.type

    def to_internal_value(self, data):
        # import pdb; pdb.set_trace()
        if type(data) == str:
            return DoctorType.objects.get(type=data)
        else:
            return DoctorType.objects.get(type=data['type'])
        return DoctorType()

class DoctorSerializer(serializers.ModelSerializer):
    types = DoctorTypeSerializer(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        types = validated_data.pop('types')
        instance = Doctor.objects.create(**validated_data)
        for type in types:
            instance.types.add(type)
        return instance

    def update(self, instance, validated_data):
        if 'types' in validated_data:
            instance.types.clear()
            types = validated_data.pop('types')
            for type in types:
                instance.types.add(type)
        return super().update(instance, validated_data)

    def to_representation(self,instance):
        representation = super(DoctorSerializer, self).to_representation(instance)
        representation['types'] = DoctorTypeSerializer(instance.types.all(), many=True).data
        return representation 