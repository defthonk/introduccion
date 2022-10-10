from argparse import Namespace
from django.contrib import admin
from django.urls import path, include #++

from .views import HomeView #++ #el . hace referencia al mismo folder que esta  ubicado y colocamos al lado que queremos llamado y lo que queremos importar 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home"), #++

    path('blog/',include('blog.urls', namespace='blog')) #++
]
