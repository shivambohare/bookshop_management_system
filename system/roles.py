from rest_framework import generics,authentication,permissions,status
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer, GenreSerializer, LanguageSerializer, AuthorSerializer, InventorySerializer, UserSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

def is_auditor(user):
    if user.is_authenticated:
        if 'auditor' in user.role:
            return True
    return False

def is_admin(user):
    if user.is_authenticated:
        if 'admin' in user.role:
            return True
    return False

def is_student(user):
    if user.is_authenticated:
        if 'student' in user.role:
            return True
    return False
