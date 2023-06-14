from django.contrib import admin
from payments.models import Payment

# Register your models here.


@admin.register(Payment)
class Payment_admin(admin.ModelAdmin):
    list_display = ['id', 'table','status_payment', 'payment_type', 'created_at']