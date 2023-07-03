from rest_framework import serializers
from container.models import *


class ReceipeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__'

class categorylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceipeCategory
        fields = '__all__'








#-------------------On_click_Items---------------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ReceipeProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['procedure_id','description']


class ReceipeCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceipeCategory
        fields = ['category_name']


class ReceipeIngredientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name']

class ReceipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_id=ReceipeIngredientDetailSerializer()
    class Meta:
        model = ReceipeIngredient
        fields = ['ingredient_id','amount','unit']

class ReceipeSerializer(serializers.ModelSerializer):
    receipe_ingredients = ReceipeIngredientSerializer(many=True, source='ingredient_receipe')
    category_id=ReceipeCategoryDetailSerializer()
    procedure_detail=ReceipeProcedureSerializer(many=True,source='procedure_receipe')
    receipe_user_id=UserSerializer()
    
    class Meta:
        model = Receipe
        fields = '__all__'
