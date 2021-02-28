from rest_framework.urlpatterns import format_suffix_patterns
from system import views
from django.urls import path

urlpatterns = [
    path('users/list/', views.UserList.as_view()),

    path('book/list/', views.BookListView.as_view()),
    path('book/create', views.BookCreateView.as_view()),
    path('book/<int:pk>/retrieve', views.BookRetrieveView.as_view()),
    path('book/<int:pk>/update', views.BookUpdateView.as_view()),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view()),

    path('genre/list/', views.GenreListView.as_view()),
    path('genre/create', views.GenreCreateView.as_view()),
    path('genre/<int:pk>/retrieve', views.GenreRetrieveView.as_view()),
    path('genre/<int:pk>/update', views.GenreUpdateView.as_view()),
    path('genre/<int:pk>/delete', views.GenreDeleteView.as_view()),

    path('language/list/', views.LanguageListView.as_view()),
    path('language/create', views.LanguageCreateView.as_view()),
    path('language/<int:pk>/retrieve', views.LanguageRetrieveView.as_view()),
    path('language/<int:pk>/update', views.LanguageUpdateView.as_view()),
    path('language/<int:pk>/delete', views.LanguageDeleteView.as_view()),

    path('author/list/', views.AuthorListView.as_view()),
    path('author/create', views.AuthorCreateView.as_view()),
    path('author/<int:pk>/retrieve', views.AuthorRetrieveView.as_view()),
    path('author/<int:pk>/update', views.AuthorUpdateView.as_view()),
    path('author/<int:pk>/delete', views.AuthorDeleteView.as_view()),

    path('inventory/list/', views.InventoryListView.as_view()),
    path('inventory/create', views.InventoryCreateView.as_view()),
    path('inventory/<str:pk>/retrieve', views.InventoryRetrieveView.as_view()),
    path('inventory/<str:pk>/update', views.InventoryUpdateView.as_view()),
    path('inventory/<str:pk>/delete', views.InventoryDeleteView.as_view()),
    path('lendbook', views.LendBookView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
