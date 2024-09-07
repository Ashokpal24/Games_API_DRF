from django.urls import path, include

from publisher.views import PublisherViewSet
from developer.views import DeveloperViewSet
from game.views import GameViewSet
from order.views import (OrderPostViewSet, OrderListViewSet)
from user.views import (user_list, create_user, user_detail)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'publisher', PublisherViewSet)
router.register(r'developer', DeveloperViewSet)
router.register(r'game', GameViewSet)
router.register(r'order-post', OrderPostViewSet, basename="order-post")
router.register(r'order', OrderListViewSet)


user_urlpatterns = [
    path("users/", user_list, name='user-list'),
    path("users/create/", create_user, name='user-add'),
    path("users/<int:pk>", user_detail, name='user-detail'),
]

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include(user_urlpatterns)),
    path("", include(router.urls)),
]
