from django.contrib import admin
from django.urls import path
from spesometro.views import simple_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', simple_upload, name="import")
]
