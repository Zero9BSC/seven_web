from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contact', include('Contact.urls')),
    path('', include('Home.urls')),
    path('', include('Multimedia.urls')),
    #path('', include('Shop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
