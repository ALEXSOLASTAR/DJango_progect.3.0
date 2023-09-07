from django.urls import path

from progects.views import *
from progects.views import ProgectDetailVaiew

urlpatterns = [
    path('', ProgectListView.as_view(), name='home'),
    #path('', home, name='home'),
    path('detail/<int:pk>/', ProgectDetailVaiew.as_view(), name='detail'),
    path('add/', ProgectCreateView.as_view(), name='creat'),
    path('update/<int:pk>/', ProgectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProgectDeleteView.as_view(), name='delete'),
]