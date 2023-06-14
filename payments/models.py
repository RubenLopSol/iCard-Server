from django.db import models

# Create your models here.

Payment_type_enum = (
    ("CARD", "card"),
    ("CASH", "cash")
)

Status_payment_enum = (
    ("PENDING", "pending"),
    ("PAID", "paid")
)


class Payment(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=255, choices=Payment_type_enum)
    status_payment = models.CharField(max_length=255, choices=Status_payment_enum)
    created_at = models.DateField(auto_now_add=True)


    def __sel__(self):

        return str(self.table)