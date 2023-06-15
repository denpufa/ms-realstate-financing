from django.core.exceptions import ValidationError

class RealStateLoanValidator:

    MINIMUN_ENTRY_PERCENT = 0.1

    MAXIMUN_INCOME_PER_MONTH = 0.3

    def validate_entry_value(self,entry_value:float,total_value:float):

        if entry_value < total_value*self.MINIMUN_ENTRY_PERCENT:
            return ValidationError({"error":"O valor minimo da entrada é 10%"})

    def validate_monthly_income(self,monthly_income:float,total_value_per_month:float):

        if monthly_income*self.MAXIMUN_INCOME_PER_MONTH > total_value_per_month:
            return ValidationError({"error":"O valor da parcela não pode ser superior a 30% da renda mensal"})

    def validate_number_of_installments(self,number_of_installments:int):

        if number_of_installments % 12 != 0:
            return ValidationError({"error":"O número de parcelas deve ser mutiplo de 12"})

