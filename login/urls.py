from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^', include('home.urls')),
    url(r'^account/', include('social_django.urls', namespace='social')),
    url(r'^account/', include(('django.contrib.auth.urls', 'auth'), namespace='auth')),
    url(r'^admin/', admin.site.urls),
]