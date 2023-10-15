from django.urls import include, path
from rest_framework import routers
from coffee.views import CoffeeViewSet

router = routers.DefaultRouter()
router.register(r'coffees', CoffeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]