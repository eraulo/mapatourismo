from django.conf.urls import url
from tourismo import views

urlpatterns=[
        url(r'^$', views.Tourismo.as_view(), name="tourismo")
]
