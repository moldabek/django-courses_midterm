from django.urls import path
from . import views
urlpatterns = [
    path('books/', views.BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>/', views.BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'})),
    path('journals/', views.JournalViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('journals/<int:pk>/', views.JournalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete'})),

]
