"""hyou8_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from hyou8_api.models import ProvinceCity
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class ProvinceCitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProvinceCity
        fields = ('name', 'pid')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = ProvinceCity.objects.all()
    serializer_class = ProvinceCitySerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'province', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
