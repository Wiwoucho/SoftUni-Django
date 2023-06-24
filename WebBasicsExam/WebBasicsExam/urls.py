
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebBasicsExam.common.urls')),
    path('<int:pk>/', include('WebBasicsExam.fruit_id.urls')),
    path('profile/', include('WebBasicsExam.user_profile.urls'))
]
