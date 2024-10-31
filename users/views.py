from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView

from users.models import User, Payments
from users.serliazers import UserSerializer, PaymentsSerializer


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

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

