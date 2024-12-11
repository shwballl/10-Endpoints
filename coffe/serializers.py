from rest_framework import serializers
from rest_framework.renderers import JSONRenderer



class CoffeSerializer(serializers.Serializer):
	tittle = serializers.CharField(max_length=255)
	content = serializers.CharField()
	cat_id = serializers.IntegerField()

class CatSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=255)

class TasteSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=255)

class FavSerializer(serializers.Serializer):
	tittle = serializers.CharField(max_length=255)
	content = serializers.CharField()
	cat_id = serializers.IntegerField()

class AllergensSerializer(serializers.Serializer):
	content = serializers.CharField()
	coffe_cat_id = serializers.IntegerField()

class StoresSerializer(serializers.Serializer):
	address = serializers.CharField()

class OrdersSerializer(serializers.Serializer):
	content = serializers.CharField()
	date = serializers.DateField()

class RewardsSerializer(serializers.Serializer):
	content = serializers.CharField()
	date = serializers.DateField()

class SpecialsSerializer(serializers.Serializer):
	tittle = serializers.CharField(max_length=255)
	content = serializers.CharField()
	cat_id = serializers.IntegerField()