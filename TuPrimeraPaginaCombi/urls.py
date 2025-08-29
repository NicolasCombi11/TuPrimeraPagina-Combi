
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('blog/', include('blog.urls')),
    path('pages/', post_list, name='pages'),
    path('pages/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),               
    path('accounts/', include('django.contrib.auth.urls')),
    path('messages/', include('messaging.urls', namespace='messaging')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)