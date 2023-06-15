from django.db import models
from .manager import DefaultEntityManager, ActiveBaseEntityManager
import uuid

class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True)

    active = ActiveBaseEntityManager()
    objects = DefaultEntityManager()

class RealStateLoanAbstract(BaseModel):
    class Meta:
        abstract = True

    real_state_total_value = models.FloatField()
    entry_value = models.FloatField()
    loan_total_value = models.FloatField()
    monthly_income = models.FloatField()
    number_of_installments = models.IntegerField()
    user_id = models.CharField(max_length=255)
    interest_rate_per_year = models.FloatField()
    value_per_month = models.FloatField()

class RealStateLoan(RealStateLoanAbstract):

    installments_payed = models.IntegerField(default=0)

class RealStateLoanSimulation(RealStateLoanAbstract):
    pass

class Fee(BaseModel):

    fee_percent = models.FloatField(default=12.0)