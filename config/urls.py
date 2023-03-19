import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path, include


urlpatterns = [
    path("", include('main.urls')),

    path('admin/', admin.site.urls),
    
    # Django Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),
]


# Para que las imagnes se puedan ver en develop
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "Administración del Sitio"  
admin.site.site_title  =  "Administración del Sitio"
admin.site.index_title  =  "Administración"
admin.site.unregister(Group)
