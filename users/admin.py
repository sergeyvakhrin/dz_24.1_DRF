from django.contrib import admin

from users.models import User, Subscription, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'last_login']
    list_display_links = ['id', 'email']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscription_name', 'user', 'course', 'subscription_sign']


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_amount', 'session_id', 'status_pay']
