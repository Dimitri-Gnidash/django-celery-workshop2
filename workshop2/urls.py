from django.conf.urls import patterns, url
from views import ScaleImageView

urlpatterns = patterns('',
    url(r'^$', ScaleImageView.as_view(), name='home'),
)
