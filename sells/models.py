from django.db import models
from django.utils.translation import gettext_lazy as _
from members.models import CustomUser

# Create your models here.
class Purchase(models.Model):
    purchase_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, related_name="user_purchases", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = _("Purchase")
        verbose_name_plural = _("Purchases")

    def __str__(self):
        return self.name


class Return(models.Model):
    return_id = models.BigAutoField(primary_key=True)
    purchase = models.OneToOneField(Purchase, related_name="returns", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="user_refund", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    reason = models.TextField(null=False, blank=False)
    status = models.CharField(choices = [("P", "Pending"), ("D", "Done")], max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Return")
        verbose_name_plural = _("Returns")

    def __str__(self):
        return self.name

