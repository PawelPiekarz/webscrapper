from django.conf.urls import include, url
from django.contrib import admin

from restapp import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stats/', views.StatsForAllSite.as_view()),
    ]
