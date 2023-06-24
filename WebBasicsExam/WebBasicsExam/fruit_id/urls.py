from django.urls import path

from WebBasicsExam.fruit_id.views import fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('details/', fruit_details, name='fruit details'),
    path('edit/', fruit_edit, name='fruit edit'),
    path('delete/', fruit_delete, name='fruit delete'),
]