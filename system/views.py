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
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from .roles import *
from .messages import *
from rest_framework.exceptions import PermissionDenied
from datetime import date

#---------------------------------------- Bookshop Management System : Genre : View Classes -------------------------------------------#
class GenreListView(generics.ListAPIView):

    serializer_class = GenreSerializer

    def get_queryset(self):
        if is_admin(self.request.user):
            response = Genre.objects.all()         
            return response
        else:
            raise PermissionDenied()

#-------------------------------------------------------------------------------------------#
class GenreCreateView(generics.CreateAPIView):

    serializer_class = GenreSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                genre = Genre.objects.create()
                serializer = GenreSerializer(genre, data=request.data, partial=True)
                if serializer.is_valid():
                    ganre = serializer.save()
                return Response(model_to_dict(genre), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.GENRE_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class GenreRetrieveView(generics.ListAPIView):

    serializer_class = GenreSerializer

    def get(self, request, pk):
        if is_admin(request.user):
            try:
                response = get_object_or_404(Genre,pk=pk)
            except:
                return Response("Error: "+ERROR_MESSAGES.GENRE_404, status=status.HTTP_404_NOT_FOUND)           
            return Response(model_to_dict(response), status=status.HTTP_200_OK)        
        else:
            return Response("Error: "+ERROR_MESSAGES.GENRE_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------------------------------------------------------------#
class GenreUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = GenreSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                genre = Genre.objects.get(pk=int(request.data.dict()['id']))
                serializer = GenreSerializer(genre, data=request.data, partial=True)
                if serializer.is_valid():
                    genre = serializer.save()
                return Response(model_to_dict(genre), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.GENRE_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class GenreDeleteView(generics.DestroyAPIView):

    serializer_class = GenreSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                genre = Genre.objects.get(pk=int(request.data.dict()['id']))
                genre.delete()
                return Response("Error: "+messages.DELETE_200, status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.GENRE_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------- Bookshop Management System : Language : View Classes -----------------------------------------#
class LanguageListView(generics.ListAPIView):

    serializer_class = LanguageSerializer

    def get_queryset(self):
        if is_admin(self.request.user):
            response = Language.objects.all()         
            return response
        else:
            raise PermissionDenied()

#--------------------------------------------------------------------------------------------#
class LanguageCreateView(generics.CreateAPIView):

    serializer_class = LanguageSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                language = Language.objects.create()
                serializer = LanguageSerializer(language, data=request.data, partial=True)
                if serializer.is_valid():
                    language = serializer.save()
                return Response(model_to_dict(language), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.LANGUAGE_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class LanguageRetrieveView(generics.ListAPIView):

    serializer_class = LanguageSerializer

    def get(self, request, pk):
        if is_admin(request.user):
            try:
                response = get_object_or_404(Language,pk=pk)
            except:
                return Response("Error: "+ERROR_MESSAGES.LANGUAGE_404, status=status.HTTP_404_NOT_FOUND)           
            return Response(model_to_dict(response), status=status.HTTP_200_OK)        
        else:
            return Response("Error: "+ERROR_MESSAGES.LANGUAGE_403, status=status.HTTP_403_FORBIDDEN)


#--------------------------------------------------------------------------------------------#
class LanguageUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = LanguageSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                language = Language.objects.get(pk=int(request.data.dict()['id']))
                serializer = LanguageSerializer(language, data=request.data, partial=True)
                if serializer.is_valid():
                    language = serializer.save()
                return Response(model_to_dict(language), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.LANGUAGE_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class LanguageDeleteView(generics.DestroyAPIView):

    serializer_class = LanguageSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                language = Language.objects.get(pk=int(request.data.dict()['id']))
                language.delete()
                return Response("Error: "+messages.DELETE_200, status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.LANGUAGE_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------- Bookshop Management System : Author : View Classes -----------------------------------------#
class AuthorListView(generics.ListAPIView):

    serializer_class = AuthorSerializer

    def get_queryset(self):
        if is_admin(self.request.user):
            response = Author.objects.all()         
            return response
        else:
            raise PermissionDenied()

#--------------------------------------------------------------------------------------------#
class AuthorCreateView(generics.CreateAPIView):

    serializer_class = AuthorSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                author = Author.objects.create()
                serializer = AuthorSerializer(author, data=request.data, partial=True)
                if serializer.is_valid():
                    author = serializer.save()
                return Response(model_to_dict(author), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.AUTHOR_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class AuthorRetrieveView(generics.ListAPIView):

    serializer_class = AuthorSerializer

    def get(self, request, pk):
        if is_admin(request.user):
            try:
                response = get_object_or_404(Author,pk=pk)
            except:
                return Response("Error: "+ERROR_MESSAGES.AUTHOR_404, status=status.HTTP_404_NOT_FOUND)           
            return Response(model_to_dict(response), status=status.HTTP_200_OK)        
        else:
            return Response("Error: "+ERROR_MESSAGES.AUTHOR_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class AuthorUpdateView(generics.RetrieveUpdateAPIView):

    serializer_class = AuthorSerializer

    def post(self, request):
        if is_admin(request.user):
            try:

                author = Author.objects.get(pk=int(request.data.dict()['id']))
                serializer = AuthorSerializer(author, data=request.data, partial=True)
                if serializer.is_valid():
                    author = serializer.save()
                return Response(model_to_dict(author), status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.AUTHOR_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class AuthorDeleteView(generics.DestroyAPIView):
 
    serializer_class = AuthorSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                author = Author.objects.get(pk=int(request.data.dict()['id']))
                author.delete()
                return Response("Error: "+messages.DELETE_200, status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.AUTHOR_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------- Bookshop Management System : Book : View Classes -----------------------------------------#
class BookListView(generics.ListAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
#--------------------------------------------------------------------------------------------#
class BookCreateView(generics.CreateAPIView):
    
    def post(self, request):
        if is_admin(request.user):
            try:
                book = Book.objects.create()
                if 'author' in request.data.dict().keys():                    
                    var = int(request.data.dict().get('author'))
                    try:
                        book.author = get_object_or_404(Author,pk=var)                    
                    except:
                        return Response("Error: "+ERROR_MESSAGES.AUTHOR_404, status=status.HTTP_404_NOT_FOUND)
                if 'genre' in request.data.dict().keys():
                    var = int(request.data.dict().get('genre'))
                    try:
                        book.genre = get_object_or_404(Genre,pk=var)
                    except:
                        return Response("Error: "+ERROR_MESSAGES.GENRE_404, status=status.HTTP_404_NOT_FOUND)
                if 'language' in request.data.dict().keys():
                    var = int(request.data.dict().get('language'))
                    try:
                        book.language = get_object_or_404(Language,pk=var)
                    except:
                        return Response("Error: "+ERROR_MESSAGES.LANGUAGE_404, status=status.HTTP_404_NOT_FOUND)
                serializer = BookSerializer(book, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response(model_to_dict(book), status=status.HTTP_200_OK)
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: "+ERROR_MESSAGES.BOOK_403, status=status.HTTP_403_FORBIDDEN)
#--------------------------------------------------------------------------------------------#
class BookRetrieveView(generics.ListAPIView):

    def get(self, request, pk):
        if is_admin(request.user) or is_student(request.user):
            try:
                response = get_object_or_404(Book,pk=pk)
                if response:
                    response_dict = model_to_dict(response)
                    if response.author:
                        author = Author.objects.filter(id = response.author.id)
                        response_dict.update(author = model_to_dict(author.first()))
                    if response.genre:
                        genre = Genre.objects.filter(id = response.genre.id)
                        response_dict.update(genre = model_to_dict(genre.first()))
                    if response.language:
                        language = Language.objects.filter(id = response.language.id)
                        response_dict.update(language = model_to_dict(language.first()))    
            except:
                return Response("Error: "+ERROR_MESSAGES.BOOK_404, status=status.HTTP_404_NOT_FOUND)           
            return Response(response_dict, status=status.HTTP_200_OK)        
        else:
            return Response("Error: "+ERROR_MESSAGES.BOOK_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class BookUpdateView(generics.RetrieveUpdateAPIView):

    def post(self, request):
        if is_admin(request.user):
            try:
                book = Book.objects.get(pk=int(request.data.dict()['id']))
                serializer = BookSerializer(book, data=request.data, partial=True)
                if serializer.is_valid():
                    if 'author' in request.data.dict().keys():                    
                        var = int(request.data.dict().get('author'))
                        try:
                            book.author = get_object_or_404(Author,pk=var)                    
                        except:
                            return Response("Error: "+ERROR_MESSAGES.AUTHOR_404, status=status.HTTP_404_NOT_FOUND)                
                    if 'genre' in request.data.dict().keys():
                        var = int(request.data.dict().get('genre'))
                        try:
                            book.genre = get_object_or_404(Genre,pk=var)
                        except:
                            return Response("Error: "+ERROR_MESSAGES.GENRE_404, status=status.HTTP_404_NOT_FOUND)
                    if 'language' in request.data.dict().keys():
                        var = int(request.data.dict().get('language'))
                        try:
                            book.language = get_object_or_404(Language,pk=var)
                        except:
                            return Response("Error: "+ERROR_MESSAGES.LANGUAGE_404, status=status.HTTP_404_NOT_FOUND)
                    serializer.save()
                    return Response(model_to_dict(book), status=status.HTTP_200_OK)        
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: "+ERROR_MESSAGES.BOOK_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class BookDeleteView(generics.DestroyAPIView):

    serializer_class = BookSerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                book = Book.objects.get(pk=int(request.data.dict()['id']))
                try:
                    book.delete()
                except:
                    return Response("Error: Cannot delete the book instance as it is referenced in one or more inventories.", status=status.HTTP_400_BAD_REQUEST)
                return Response("Error: "+messages.DELETE_200, status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.AUTHOR_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------- Bookshop Management System : Inventory : View Classes -----------------------------------------#
class InventoryListView(generics.ListAPIView):

    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    
#--------------------------------------------------------------------------------------------#
class InventoryCreateView(generics.CreateAPIView):
   
    def post(self, request):
        if is_admin(request.user):
            try:
                try:
                    var = int(request.data.dict().get('book'))
                except:
                    return Response("Error: ", status=status.HTTP_404_NOT_FOUND)
                try:    
                    book = get_object_or_404(Book,pk=var)                    
                except:
                    return Response("Error: "+ERROR_MESSAGES.BOOK_404, status=status.HTTP_404_NOT_FOUND)
                inventory = Inventory.objects.create(book=book, status='a')
                serializer = InventorySerializer(inventory, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response(model_to_dict(inventory), status=status.HTTP_200_OK)       
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: "+ERROR_MESSAGES.INVENTORY_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class InventoryRetrieveView(generics.ListAPIView):

    def get(self, request, pk):
        try:
            response = get_object_or_404(Inventory,pk=pk)
        except:
            return Response("Error: "+ERROR_MESSAGES.INVENTORY_404, status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(response), status=status.HTTP_200_OK)

#--------------------------------------------------------------------------------------------#
class InventoryUpdateView(generics.RetrieveUpdateAPIView):

    def post(self, request):
        if is_admin(request.user):
            try:
                inventory = Inventory.objects.get(pk=request.data.dict()['id'])
                serializer = InventorySerializer(inventory, data=request.data, partial=True)
                if serializer.is_valid():
                    if 'book' in request.data.dict().keys():
                        var = int(request.data.dict().get('book'))
                        try:
                            inventory.book = get_object_or_404(Book,pk=var)
                        except:
                            return Response("Error: "+ERROR_MESSAGES.BOOK_404, status=status.HTTP_404_NOT_FOUND)
                    if 'borrower' in request.data.dict().keys():
                        var = int(request.data.dict().get('borrower'))
                        try:
                            inventory.borrower = get_object_or_404(User,pk=var)
                        except:
                            return Response("Error: "+ERROR_MESSAGES.BORROWER_404, status=status.HTTP_404_NOT_FOUND)
                    serializer.save()
                    return Response(model_to_dict(inventory), status=status.HTTP_200_OK)       
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: "+ERROR_MESSAGES.INVENTORY_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class InventoryDeleteView(generics.CreateAPIView):

    serializer_class = InventorySerializer

    def post(self, request):
        if is_admin(request.user):
            try:
                inventory = Inventory.objects.get(pk=request.data.dict()['id'])
                inventory.delete()
                return Response("Error: "+messages.DELETE_200, status=status.HTTP_200_OK)  
            except:
                return Response("Bad Request",status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response("Error: "+ERROR_MESSAGES.INVENTORY_403, status=status.HTTP_403_FORBIDDEN)

#--------------------------------------------------------------------------------------------#
class LendBookView(generics.ListCreateAPIView):

    def post(self, request):
        if is_admin(request.user) or is_student(request.user):
            try:
                var = int(request.data.dict().get('book'))
                try:
                    book = get_object_or_404(Book,pk=var) 
                except:
                    return Response("Error: "+ERROR_MESSAGES.BOOK_404, status=status.HTTP_404_NOT_FOUND)
                try:
                    inventory = Inventory.objects.filter(book__id=var).filter(status='a')
                    if not inventory:
                        return Response("Error: "+ERROR_MESSAGES.COPIES_404, status=status.HTTP_404_NOT_FOUND)
                except:
                    return Response("Error: "+ERROR_MESSAGES.COPIES_404, status=status.HTTP_404_NOT_FOUND)
                inventory_lend = inventory.first()
                serializer = InventorySerializer(inventory_lend, data=request.data, partial=True)
                inventory_lend.status='l'
                if serializer.is_valid():
                    serializer.save()
                return Response(model_to_dict(inventory_lend), status=status.HTTP_200_OK)
            except:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Error: "+ERROR_MESSAGES.INVENTORY_403, status=status.HTTP_403_FORBIDDEN)

#---------------------------------------- Bookshop Management System : User : View Classes -----------------------------------------#
class UserList(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        if is_admin(self.request.user):
            response = User.objects.all()         
            return response
        else:
            raise PermissionDenied()

class UserCreate(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]