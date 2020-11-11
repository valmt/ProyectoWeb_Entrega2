
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include('PaginaWebApp.urls')),
]

urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls'))


]
