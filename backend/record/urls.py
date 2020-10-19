from . import views
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'top/$', csrf_exempt(views.TopRecordsView.as_view())),
]
