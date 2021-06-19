from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from albums import views as albums_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', albums_views.list_albums, name='list_albums'),
]
