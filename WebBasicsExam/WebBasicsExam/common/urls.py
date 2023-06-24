from django.urls import path

from WebBasicsExam.common.views import dashboard, create, index

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create, name='create')
]