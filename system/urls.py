from rest_framework.urlpatterns import format_suffix_patterns
from system import views
from django.urls import path

urlpatterns = [
    path('user/list/', views.UserList.as_view()),
    path('user/register', views.UserCreate.as_view()),

    path('book/list/', views.BookListView.as_view()),
    path('book/create', views.BookCreateView.as_view()),
    path('book/update', views.BookUpdateView.as_view()),
    path('book/delete', views.BookDeleteView.as_view()),
    path('book/<int:pk>', views.BookRetrieveView.as_view()),

    path('genre/list/', views.GenreListView.as_view()),
    path('genre/create', views.GenreCreateView.as_view()),
    path('genre/update', views.GenreUpdateView.as_view()),
    path('genre/delete', views.GenreDeleteView.as_view()),
    path('genre/<int:pk>', views.GenreRetrieveView.as_view()),

    path('language/list/', views.LanguageListView.as_view()),
    path('language/create', views.LanguageCreateView.as_view()),
    path('language/update', views.LanguageUpdateView.as_view()),
    path('language/delete', views.LanguageDeleteView.as_view()),
    path('language/<int:pk>', views.LanguageRetrieveView.as_view()),

    path('author/list/', views.AuthorListView.as_view()),
    path('author/create', views.AuthorCreateView.as_view()),
    path('author/update', views.AuthorUpdateView.as_view()),
    path('author/delete', views.AuthorDeleteView.as_view()),
    path('author/<int:pk>', views.AuthorRetrieveView.as_view()),

    path('inventory/list/', views.InventoryListView.as_view()),
    path('inventory/create', views.InventoryCreateView.as_view()),
    path('inventory/delete', views.InventoryDeleteView.as_view()),
    path('inventory/update', views.InventoryUpdateView.as_view()),
    path('inventory/<str:pk>', views.InventoryRetrieveView.as_view()),
    path('lendbook', views.LendBookView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
