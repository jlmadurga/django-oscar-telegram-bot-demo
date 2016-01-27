from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from oscar.app import application
from oscar.views import handler500, handler404, handler403

from apps.sitemaps import base_sitemaps


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
    url(r'^i18n/', include('django.conf.urls.i18n')),

]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns('',
    # Custom functionality to allow dashboard users to be created
    url(r'gateway/', include('apps.gateway.urls')),
    # Oscar's normal URLs
    url(r'', include(application.urls)),
)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
