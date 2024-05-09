from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/', include("adminpanel.urls")),
    path('', include("market.urls")),
    path('auth/', include("users.urls")),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)