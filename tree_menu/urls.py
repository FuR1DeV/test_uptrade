from django.contrib import admin
from django.urls import path

from menu.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', Index.as_view(), name='index'),
    path('', Index.as_view())
]
