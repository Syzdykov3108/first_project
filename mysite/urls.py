from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
