from django.db import models


class Payment(models.Model):
    """
    This model use for registeration payments.
    """

    full_name = models.CharField(
        verbose_name="Full name", max_length=255, blank=True, null=True
    )
    amount = models.BigIntegerField(
        verbose_name="Amount"
    )
    mobile = models.CharField(
        verbose_name="Mobile number", max_length=11, blank=True, null=True
    )
    description = models.CharField(
        verbose_name="Description", max_length=255, blank=True, null=True
    )
    transid = models.IntegerField(
        verbose_name="Trans ID"
    )
    status = models.BooleanField(
        verbose_name="Status", default=False
    )
    card_number = models.BigIntegerField(
        verbose_name="Card number", blank=True, null=True
    )
    trace_number = models.BigIntegerField(
        verbose_name="Trace number", blank=True, null=True
    )
    message = models.TextField(
        verbose_name="Message", blank=True, null=True
    )
