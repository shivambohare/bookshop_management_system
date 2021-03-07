from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

#---------------------------------------- Bookshop Management System : User : Model Class -----------------------------------------#
class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('auditor', 'auditor'),
        ('student', 'student'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
    )

#---------------------------------------- Bookshop Management System : Genre : Model Class -----------------------------------------#
class Genre(models.Model):
    """Model: Genres"""

    genre = models.CharField(max_length=30, help_text='Book Genre (e.g. Narrative Non-Fiction)')

    def __str__(self):
        return self.genre

#---------------------------------------- Bookshop Management System : Language : Model Class ----------------------------------------#
class Language(models.Model):
    """Model: Languages"""

    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language

#---------------------------------------- Bookshop Management System : Author : Model Class -----------------------------------------#
class Author(models.Model):
    """Model: Authors"""

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    number_of_books = models.IntegerField(default=0, verbose_name=("Number of Books Published"))

    class Meta:
        ordering = ['number_of_books', 'first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

#---------------------------------------- Bookshop Management System : Book : Model Class -----------------------------------------#
class Book(models.Model):
    """Model: Books"""

    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, help_text='Select author for this book', on_delete=models.SET_NULL, null= True)
    genre = models.ForeignKey(Genre, help_text='Select genre for this book',on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    @property
    def author_name(self):
        return self.author.first_name


#---------------------------------------- Bookshop Management System : Inventory : Model Class -----------------------------------------#
class Inventory(models.Model):
    """Model: Inventory"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    version = models.CharField(max_length=20)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="book_borrower", null=True, blank=True,)
    borrow_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    BOOK_STATUS = (
        ('l', 'Lent'),
        ('a', 'Available'),
        ('b', 'Booked'),
        ('r', 'Reserved')
    )
    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['status']
        verbose_name_plural = "Inventories"

    def __str__(self):
        return f'{self.id} ({self.book.name})'
