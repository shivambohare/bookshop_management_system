from rest_framework import serializers
from .models import *

#---------------------------------------- Bookshop Management System : Genre : Serializer Classes -----------------------------------------#
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')

#---------------------------------------- Bookshop Management System : Language : Serializer Classes ---------------------------------------#
class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ('__all__')

#---------------------------------------- Bookshop Management System : Author : Serializer Classes ----------------------------------------#
class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author       
        fields = ('__all__')

#---------------------------------------- Bookshop Management System : Book : Serializer Classes ------------------------------------------#
class BookSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('__all__')
        depth = 1

#---------------------------------------- Bookshop Management System : User : Serializer Classes -----------------------------------------#
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')

    def create(self, validated_data):
        if 'student' in validated_data['role'] or 'auditor' in validated_data['role']:
            user = User()
            password = validated_data.pop('password')
            user.username = validated_data['username']
            user.role = validated_data['role']
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError("Error: The role can only be student or auditor")

#---------------------------------------- Bookshop Management System : Inventory : Serializer Classes -------------------------------------#
class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('__all__')
        depth = 1
