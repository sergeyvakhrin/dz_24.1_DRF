from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet, UserCreateAPIView, SubscriptionCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router_payments = DefaultRouter()
router_payments.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    # path('subscription/update/', SubscriptionUpdateAPIView.as_view(), name='subscription-update'),
] + router.urls + router_payments.urls

