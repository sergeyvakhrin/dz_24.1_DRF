from django.contrib import admin

from users.models import User, Subscription, Payments

admin.site.register(User)

admin.site.register(Subscription)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_amount', 'session_id', 'status_pay']
