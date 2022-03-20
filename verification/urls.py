
from django.urls import re_path

urlpatterns = [
    re_path(r'^smscode/(?P<mobile>1[3-9]\d(9)/$)'),
]
