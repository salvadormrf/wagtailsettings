from django.conf.urls import url
from wagtailsettings import views


urlpatterns = [
    url(r'^$', views.index, name='wagtailsettings_index'),
    url(r'^(\w+)/(\w+)/$', views.edit, name='wagtailsettings_edit'),
]
