from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls , name="adminpanel"),
    path('dashboard/', include("apps.adminpanel.urls")),
    path('', include("apps.market.urls")),
    path('auth/', include("apps.users.urls")),    
    path('payment/', include("apps.payment.urls")),
]
if not settings.DEBUG:
    urlpatterns+= staticfiles_urlpatterns()
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+= staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)