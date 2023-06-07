from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewset

router_category = DefaultRouter()
router_category.register(
    prefix= 'categories', basename= 'categories', viewset= CategoryApiViewset
)