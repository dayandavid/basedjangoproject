import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import include, path

urlpatterns = [
    path("", include('main.urls')),
    path('admin/login/', admin.site.login, name='admin_login'),

    path('admin/', admin.site.urls),
    
    # Django Debug Toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    # Captcha
    path('captcha/', include('captcha.urls')),

    # All Auth
    path("accounts/", include("allauth.urls")),
]


# Para que las imagenes se puedan ver en develop
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "Administración del Sitio"  
admin.site.site_title  =  "Administración del Sitio"
admin.site.index_title  =  "Administración"
admin.site.unregister(Group)
