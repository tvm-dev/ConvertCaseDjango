from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    #App Core
    path('', include('core.urls', namespace='pages_tvm')),

    #App Admin Django
    path('admin/', admin.site.urls),
   
]






