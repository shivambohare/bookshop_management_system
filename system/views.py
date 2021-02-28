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

#---------------------------------------- Bookshop Management System : Genre : View Classes -------------------------------------------#
class GenreListView(generics.ListAPIView):

    queryset = Genre.objects.all()

    serializer_class = GenreSerializer

#-------------------------------------------------------------------------------------------#
class GenreCreateView(generics.CreateAPIView):

    queryset = Genre.objects.all()

    serializer_class = GenreSerializer

#--------------------------------------------------------------------------------------------#
class GenreRetrieveView(generics.ListAPIView):

    serializer_class = GenreSerializer

    def get(self, request, pk):

        try:

            response = get_object_or_404(Genre,pk=pk)

        except:

            return Response("error message: Genre does not exist", status=status.HTTP_404_NOT_FOUND)
        
        return Response(model_to_dict(response), status=status.HTTP_200_OK)

#---------------------------------------------------------------------------------------------#
class GenreUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Genre.objects.all()

    serializer_class = GenreSerializer

#--------------------------------------------------------------------------------------------#
class GenreDeleteView(generics.DestroyAPIView):

    queryset = Genre.objects.all()

    serializer_class = GenreSerializer

#---------------------------------------- Bookshop Management System : Language : View Classes -----------------------------------------#
class LanguageListView(generics.ListAPIView):

    queryset = Language.objects.all()

    serializer_class = LanguageSerializer

#--------------------------------------------------------------------------------------------#
class LanguageCreateView(generics.CreateAPIView):

    queryset = Language.objects.all()

    serializer_class = LanguageSerializer

#--------------------------------------------------------------------------------------------#
class LanguageRetrieveView(generics.ListAPIView):
    serializer_class = LanguageSerializer

    def get(self, request, pk):

        try:

            response = get_object_or_404(Language,pk=pk)

        except:

            return Response("error message: Language does not exist", status=status.HTTP_404_NOT_FOUND)
        
        return Response(model_to_dict(response), status=status.HTTP_200_OK)


#--------------------------------------------------------------------------------------------#
class LanguageUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Language.objects.all()

    serializer_class = LanguageSerializer

#--------------------------------------------------------------------------------------------#
class LanguageDeleteView(generics.DestroyAPIView):

    queryset = Language.objects.all()

    serializer_class = LanguageSerializer

#---------------------------------------- Bookshop Management System : Author : View Classes -----------------------------------------#
class AuthorListView(generics.ListAPIView):

    queryset = Author.objects.all()

    serializer_class = AuthorSerializer

#--------------------------------------------------------------------------------------------#
class AuthorCreateView(generics.CreateAPIView):
   
    queryset = Author.objects.all()
    
    serializer_class = AuthorSerializer

#--------------------------------------------------------------------------------------------#
class AuthorRetrieveView(generics.ListAPIView):

    serializer_class = AuthorSerializer

    def get(self, request, pk):

        response = Author.objects.get(pk=pk)
        
        return Response(model_to_dict(response), status=status.HTTP_200_OK)

#--------------------------------------------------------------------------------------------#
class AuthorUpdateView(generics.RetrieveUpdateAPIView):
   
    queryset = Author.objects.all()
   
    serializer_class = AuthorSerializer

#--------------------------------------------------------------------------------------------#
class AuthorDeleteView(generics.DestroyAPIView):

    queryset = Author.objects.all()
    
    serializer_class = AuthorSerializer

#---------------------------------------- Bookshop Management System : Book : View Classes -----------------------------------------#
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer
    
#--------------------------------------------------------------------------------------------#
class BookCreateView(generics.CreateAPIView):
    
    def post(self, request):

        try:

            book = Book.objects.create()

            if 'author' in request.data.dict().keys():
                    
                var = int(request.data.dict().get('author'))

                try:

                    book.author = get_object_or_404(Author,pk=var)
                    
                except:

                    return Response("error message: Author does not exist", status=status.HTTP_404_NOT_FOUND)

            if 'genre' in request.data.dict().keys():

                var = int(request.data.dict().get('genre'))

                try:

                    book.genre = get_object_or_404(Genre,pk=var)

                except:

                    return Response("error message: Genre does not exist", status=status.HTTP_404_NOT_FOUND)

            if 'language' in request.data.dict().keys():

                var = int(request.data.dict().get('language'))

                try:

                    book.language = get_object_or_404(Language,pk=var)

                except:

                    return Response("error message: Language does not exist", status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer(book, data=request.data, partial=True)

            if serializer.is_valid():

                serializer.save()

            return Response(model_to_dict(book), status=status.HTTP_200_OK)
        
        except:

            return Response("error", status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------------------------------------------------#
class BookRetrieveView(generics.ListAPIView):

    def get(self, request, pk):

        try:

            response = get_object_or_404(Book,pk=pk)

        except:

            return Response("error message: Book does not exist", status=status.HTTP_404_NOT_FOUND)
        
        return Response(model_to_dict(response), status=status.HTTP_200_OK)

#--------------------------------------------------------------------------------------------#
class BookUpdateView(generics.RetrieveUpdateAPIView):

    def post(self, request, pk):

        try:

            book = Book.objects.get(pk=pk)

            serializer = BookSerializer(book, data=request.data, partial=True)

            if serializer.is_valid():

                if 'author' in request.data.dict().keys():
                    
                    var = int(request.data.dict().get('author'))

                    try:

                        book.author = get_object_or_404(Author,pk=var)
                    
                    except:

                        return Response("error message: Author does not exist", status=status.HTTP_404_NOT_FOUND)
                
                if 'genre' in request.data.dict().keys():

                    var = int(request.data.dict().get('genre'))

                    try:

                        book.genre = get_object_or_404(Genre,pk=var)

                    except:

                        return Response("error message: Genre does not exist", status=status.HTTP_404_NOT_FOUND)

                if 'language' in request.data.dict().keys():

                    var = int(request.data.dict().get('language'))

                    try:

                        book.language = get_object_or_404(Language,pk=var)

                    except:

                        return Response("error message: Language does not exist", status=status.HTTP_404_NOT_FOUND)

                serializer.save()

                return Response(model_to_dict(book), status=status.HTTP_200_OK)
        
        except:

            return Response("error", status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------------------------------------------------#
class BookDeleteView(generics.DestroyAPIView):

    queryset = Book.objects.all()
    
    serializer_class = BookSerializer

#---------------------------------------- Bookshop Management System : Inventory : View Classes -----------------------------------------#
class InventoryListView(generics.ListAPIView):

    queryset = Inventory.objects.all()

    serializer_class = InventorySerializer
    
#--------------------------------------------------------------------------------------------#
class InventoryCreateView(generics.CreateAPIView):
   
    def post(self, request):

        try:

            try:

                var = int(request.data.dict().get('book'))

            except:

                return Response("error message: Book is mandatory", status=status.HTTP_404_NOT_FOUND)

            try:    

                book = get_object_or_404(Book,pk=var)
                    
            except:

                return Response("error message: Book does not exist", status=status.HTTP_404_NOT_FOUND)

            try:

                var = int(request.data.dict().get('borrower'))

            except:

                return Response("error message: Borrower is mandatory", status=status.HTTP_404_NOT_FOUND)

            try:    

                borrower = get_object_or_404(User,pk=var)
                    
            except:

                return Response("error message: User does not exist", status=status.HTTP_404_NOT_FOUND)

            inventory = Inventory.objects.create(book=book, borrower=borrower)

            serializer = InventorySerializer(inventory, data=request.data, partial=True)

            if serializer.is_valid():

                serializer.save()

            return Response(model_to_dict(inventory), status=status.HTTP_200_OK)
        
        except:

            return Response("error", status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------------------------------------------------#
class InventoryRetrieveView(generics.ListAPIView):

    def get(self, request, pk):

        try:

            response = get_object_or_404(Inventory,pk=pk)

        except:

            return Response("error message: Inventory does not exist", status=status.HTTP_404_NOT_FOUND)
        
        return Response(model_to_dict(response), status=status.HTTP_200_OK)


#--------------------------------------------------------------------------------------------#
class InventoryUpdateView(generics.RetrieveUpdateAPIView):

    def post(self, request, pk):

        try:

            inventory = Inventory.objects.get(pk=pk)

            serializer = InventorySerializer(inventory, data=request.data, partial=True)

            if serializer.is_valid():

                if 'book' in request.data.dict().keys():
                    
                    var = int(request.data.dict().get('book'))

                    try:

                        inventory.book = get_object_or_404(Book,pk=var)
                    
                    except:

                        return Response("error message: Book does not exist", status=status.HTTP_404_NOT_FOUND)
                
                if 'borrower' in request.data.dict().keys():

                    var = int(request.data.dict().get('borrower'))

                    try:

                        inventory.borrower = get_object_or_404(Genre,pk=var)

                    except:

                        return Response("error message: Borrower does not exist", status=status.HTTP_404_NOT_FOUND)

                serializer.save()

                return Response(model_to_dict(inventory), status=status.HTTP_200_OK)
        
        except:

            return Response("error", status=status.HTTP_400_BAD_REQUEST)

#--------------------------------------------------------------------------------------------#
class InventoryDeleteView(generics.DestroyAPIView):

    queryset = Inventory.objects.all()
    
    serializer_class = InventorySerializer

#--------------------------------------------------------------------------------------------#
class LendBookView(generics.ListCreateAPIView):

    def post(self, request):

        try:

            var = int(request.data.dict().get('book'))

            try:

                book = get_object_or_404(Book,pk=var)
                    
            except:

                return Response("error message: Book does not exist", status=status.HTTP_404_NOT_FOUND)

            try:

                inventory = Inventory.objects.filter(book__id=var).filter(status='a')

                if not inventory:

                    return Response("error message: No available copies exist", status=status.HTTP_404_NOT_FOUND)

            except:

                return Response("error message: No available copies exist", status=status.HTTP_404_NOT_FOUND)

            inventory_lend = inventory.first()

            serializer = InventorySerializer(inventory_lend, data=request.data, partial=True)

            inventory_lend.status='l'

            if serializer.is_valid():
                
                serializer.save()

            return Response(model_to_dict(inventory_lend), status=status.HTTP_200_OK)
        
        except:

            return Response("error", status=status.HTTP_400_BAD_REQUEST)

#---------------------------------------- Bookshop Management System : User : View Classes -----------------------------------------#
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer
