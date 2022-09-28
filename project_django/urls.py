from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
    path('todolist/', include('todolist.urls')),
]