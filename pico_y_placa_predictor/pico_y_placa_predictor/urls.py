from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
#This line is to include all the urls from validation_of_road app
    path('',include('validation_of_road.urls'))
]
