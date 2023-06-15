from rest_framework.serializers import ModelSerializer
from loan.models import (Fee,RealStateLoanSimulation,
                         RealStateLoanSimulation ,
                         RealStateLoan)
from loan.validators import RealStateLoanValidator

class FeeSerializer(ModelSerializer):

    class Meta:
        model = Fee
        exclude  = ['created_at', 'updated_at', 'is_active']

class RealStateLoanSimulationSerializer(ModelSerializer):

    class Meta:
        model = RealStateLoanSimulation
        exclude  = ['created_at', 'updated_at', 'is_active']

    def validate(self,attrs):
        attrs = super().validate(attrs)
        validator = RealStateLoanValidator()
        validator.validate_entry_value(attrs['entry_value'],
                                       attrs['real_state_total_value'])
        validator.validate_monthly_income(attrs['monthly_income'],
                                          attrs['value_per_month'])
        validator.validate_number_of_installments(attrs['number_of_installments'])

        return attrs

class RealStateLoanSerializer(ModelSerializer):

    class Meta:
        model = RealStateLoan
        exclude = ['created_at', 'updated_at','is_active']

    def validate(self,attrs):
        attrs = super().validate(attrs)
        validator = RealStateLoanValidator()
        validator.validate_entry_value(attrs['entry_value'],
                                       attrs['real_state_total_value'])
        validator.validate_monthly_income(attrs['monthly_income'],
                                          attrs['value_per_month'])
        validator.validate_number_of_installments(attrs['number_of_installments'])

        return attrs