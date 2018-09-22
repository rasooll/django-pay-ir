from django.db import models


class Payment(models.Model):
    """
    This model use for registeration payments.
    """

    full_name = models.CharField(
        name="Full name", blank=True, null=True
    )
    amount = models.BigIntegerField(
        name="Amount"
    )
    mobile = models.IntegerField(
        name="Mobile number"
    )
    description = models.CharField(
        name="Description", max_length=255, blank=True, null=True
    )
    transid = models.IntegerField(
        name="Trans ID"
    )
    status = models.BooleanField(
        name="Status", default=False
    )
    card_number = models.BigIntegerField(
        name="Card number", blank=True, null=True
    )
    trace_number = models.BigIntegerField(
        name="Trace number", blank=True, null=True
    )
    message = models.TextField(
        name="Message", blank=True, null=True
    )
