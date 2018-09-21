from django.db import models


class Invoice(models.Model):
    """
    This model use for invoices.
    """

    full_name = models.CharField(name="Full name", blank=True, null=True)
    amount = models.BigIntegerField(name="Amount")
    mobile = models.IntegerField(name="Mobile number")
    description = models.CharField(name="Description", max_length=255)
    transid = models.IntegerField(name="Trans ID")


class Payment(models.Model):
    """
    This model use for registeration payments.
    """

    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="Invoice")
    status = models.BooleanField(name="Status", default=False)
    card_number = models.BigIntegerField(name="Card number")
    trace_number = models.BigIntegerField(name="Trace number")
    message = models.TextField(name="Message")
