from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from users.models import User, Payments, Subscription
from users.serliazers import UserSerializer, PaymentsSerializer, SubscriptionSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    # Добавляем возможность фильтрации и сортировки
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # search_fields = ('paid_course', 'paid_lesson', 'payment_method', )
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method', )
    ordering_fields = ('payment_date', )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, ) # на уровне проекта все закрыто, тут открываем на регистрацию

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        """
        Проверяем, если подписка у пользователя есть, то удаляем.
        Если подписки нет, то добавляем
        """
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item:
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item, subscription_sign=True)
            message = "Подписка создана"

        return Response({"message": message})


# class SubscriptionUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()
#     permission_classes = (IsAuthenticated, )
