from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<slug>[a-z0-9A-z-]+)$',views.detail,name='detail')
]