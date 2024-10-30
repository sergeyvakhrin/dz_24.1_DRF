from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router_payments = DefaultRouter()
router_payments.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [

] + router.urls + router_payments.urls
