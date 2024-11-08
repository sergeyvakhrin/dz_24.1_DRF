from rest_framework import serializers

from users.models import User, Payments, Subscription


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class PaymentHistorySerializer(serializers.ModelSerializer):
    """ Для вывода истории платежей """
    class Meta:
        model = Payments
        fields = ('payment_date', 'payment_amount', 'payment_method')


class UserSerializer(serializers.ModelSerializer):
    # Добавление истории платежей
    payments_list = PaymentHistorySerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


