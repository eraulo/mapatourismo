from django.conf.urls import url
from tourismo import views
from django.conf.urls.static import static
from djgeojson.views import GeoJSONLayerView
from .models import Tourismo
from django.conf import settings

urlpatterns=[
        url(r'^$', views.Tourismo.as_view(), name="tourismo"),
        url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Tourismo, properties=('title', 'description', 'picture_url')), name='data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
