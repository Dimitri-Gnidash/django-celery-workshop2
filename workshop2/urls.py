from django.conf.urls import patterns, url, include
from workshop2.scale_image.views import ScaleImageView

urlpatterns = patterns('',
    url(r'^$', ScaleImageView.as_view(), name='home'),
    url(r"^celery/", include('djcelery.urls')),
)
