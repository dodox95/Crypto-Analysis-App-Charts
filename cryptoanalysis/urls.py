from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crypto/', include('cryptoapp.urls')),
    path('', include('cryptoapp.urls')), # Add this line
]
