from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('biblioteca.urls')),
    path('index/', include('biblioteca.urls')) # garantindo que o index apareça das duas formas
]
