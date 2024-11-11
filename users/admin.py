from django.contrib import admin

from users.models import User, Subscription, Payments

admin.site.register(User)

admin.site.register(Subscription)

admin.site.register(Payments)
