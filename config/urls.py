from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    path('main_panel_admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('pages.urls', namespace='pages')),
]

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    *urlpatterns,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
