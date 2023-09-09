from django.urls import path

from languages.views import *

urlpatterns = [
    path('', LanguagesListView.as_view(), name='home'),
    #path('', home, name='home'),
    path('detail/<int:pk>/', LanguagesDetailVaiew.as_view(), name='detail'),
    path('add/', LanguagesCreateView.as_view(), name='creat'),
    path('update/<int:pk>/', LanguagesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', LanguagesDeleteView.as_view(), name='delete'),
]