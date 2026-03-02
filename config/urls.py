from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Texnikum boshqaruv paneli"
admin.site.site_title = "Texnikum Admin"
admin.site.index_title = "Boshqaruv"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('talim/', include('education.urls')),
    path('kafedralar/', include('departments.urls')),
    path('uqtuvchilar/', include('faculty.urls')),
    path('yangiliklar/', include('news.urls')),
    path('hamkorlar/', include('partners.urls')),
    path('kutubxona/', include('library.urls')),
    path('yoshlar/', include('youth.urls')),
    path('aloqa/', include('contact.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)