from rest_framework.views import APIView
from rest_framework.response import Response

class SimulationRealStateLoanView(APIView):

    """
        Simulação de financiamento imobiliario,
        com corpo da requisição:
         `{
            "user_id" : "string",
            "real_state_total_value": "float",
            "entry_value" : "float",
            "monthly_income" : "float",
            "number_of_installments": "int"
        }`
    """
    def post(self,request,format=None):

      value_to_pay = request.data['real_state_total_value'] - request.data['entry_value']
      value_to_pay = value_to_pay*1.1
      value_per_month =  value_to_pay/request.data['number_of_installments']
      data = {
          'total_value': value_to_pay,
          'interest_rate_per_year': '10%',
          'value_per_month': value_per_month,
          'number_of_installments': request.data['number_of_installments']
       }

      return Response(data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateLoanView(APIView):

    """
        Financiamento imobiliario,
        com corpo da requisição:
         `{
            "user_id" : "string",
            "real_state_total_value": "float",
            "entry_value" : "float",
            "monthly_income" : "float",
            "number_of_installments": "int"
        }`
    """


    def post(self, request, format=None):

        value_to_pay = request.data['real_state_total_value'] - request.data['entry_value']
        value_to_pay = value_to_pay*1.1
        value_per_month =  value_to_pay/request.data['number_of_installments']
        data = {
            'total_value': value_to_pay,
            'interest_rate_per_year': '10%',
            'value_per_month': value_per_month,
            'number_of_installments': request.data['number_of_installments']
        }

        return Response(data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class FinancialDefermentView(APIView):

    """
        Adiantamento de parcelas do financiamento,
        com corpo da requisição:
         `{
            "deferment_total_value": "string",
            "number_of_installments": "int",
            "loan_id": "string"
        }`
    """


    def post(self, request, format=None):

        data = {
            'loan_id': request.data['loan_id'],
            'deferment_total_value': request.data['deferment_total_value'],
            'number_of_installments': request.data['number_of_installments'],
        }

        return Response(data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateLoanStatusView(APIView):

    """
        Status do financiamento imobiliario
    """


    def get(self, request, format=None):

        data = {
            "total_value_to_pay": "1.000",
            "interest_rate_per_year": "10%",
            "value_per_month": 100,
            "number_of_installments_to_pay": 5,
            "number_of_late_installments" : 0,
            "number_of_installments_payed": 5,
            "loan_id": "das91i3m1keda0131ads"
            }

        return Response(data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateFeeView(APIView):

    """
        Definição da taxa anual percentual de juros,
        com corpo da requisição:
        `{
            "fee_percent_per_year": "float"
        }`
    """

    def post(self, request, format=None):

        data =  {
            "fee_percent_per_year": 10
        }

        return Response(data,200)

    @classmethod
    def get_extra_actions(cls):
        return []



