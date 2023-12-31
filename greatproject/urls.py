from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('admin/', admin.site.urls),
	path('main-path/', include('main.urls')),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
