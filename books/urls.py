from django.urls import path
from .views import BookListAPIView, BookDetailAPIView, BookCreateAPIView, BookUpdateAPIView, BookDeleteAPIView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
    path('login/',obtain_auth_token,name="login")
    
]
