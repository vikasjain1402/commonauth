from django.conf import settings
from django.conf.urls.static import static
from pixel import urls
from django.contrib import admin
from django.urls import path,include
from django_email_verification import urls as mail_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include('accounts.urls')),
    path('email/', include(mail_urls)),
    path("",include(urls))
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)