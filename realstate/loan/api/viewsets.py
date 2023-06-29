from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (FeeSerializer,
                          RealStateLoanSerializer,
                          RealStateLoanSimulationSerializer)
from loan.models import Fee, RealStateLoan
from loan.services import LogService,IpService
from django.conf import settings
import time

BASIC_FEE = 12.0

class SimulationRealStateLoanView(APIView):

    """
        Simulação de financiamento imobiliario,
        com corpo da requisição:
         `{
            "real_state_total_value": "float",
            "entry_value" : "float",
            "monthly_income" : "float",
            "number_of_installments": "int"
        }`
    """
    def post(self,request,format=None):

        data = request.data
        value_to_pay = data['real_state_total_value'] - data['entry_value']

        #get fee
        try:
            fee = Fee.active.first().fee_percent
        except:
            fee = BASIC_FEE


        data['value_per_month'] =  value_to_pay/request.data['number_of_installments']

        #credit risck
        if data['value_per_month'] > data['monthly_income']*0.25:
            fee += 10

        data['loan_total_value'] = value_to_pay*fee/100 + value_to_pay

        data['user_id'] = request.headers['user_id']
        data['interest_rate_per_year'] = fee/(data['number_of_installments']/12)

        serializer = RealStateLoanSimulationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateLoanView(APIView):

    """
        Financiamento imobiliario,
        com corpo da requisição:
         `{
            "real_state_total_value": "float",
            "entry_value" : "float",
            "monthly_income" : "float",
            "number_of_installments": "int"
        }`
    """

    def post(self, request, format=None):

        data = request.data
        value_to_pay = data['real_state_total_value'] - data['entry_value']

        #get fee
        try:
            fee = Fee.active.first().fee_percent
        except:
            fee = BASIC_FEE

        data['value_per_month'] =  value_to_pay/request.data['number_of_installments']

        #credit risck
        if data['value_per_month'] > data['monthly_income']*0.25:
            fee += 10

        data['loan_total_value'] = value_to_pay*fee/100 + value_to_pay

        data['user_id'] = request.headers['user_id']
        data['interest_rate_per_year'] = fee/(data['number_of_installments']/12)

        serializer = RealStateLoanSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # send to log
        LogService().send_log(
            {
                "timestamp" : str(time.time()),
                "level" : "INFO",
                "microservice" : "ms-realstate-financing",
                "thread" : "main",
                "class" : self.__class__.__name__,
                "method" : "info",
                "message" : "Novo emprestimo imobiliario realizado",
                "context" : "default",
                "ip" : IpService().get_my_ip()

            })

        return Response(serializer.data,200)

    @classmethod
    def get_extra_actions(cls):
        return []

class FinancialDefermentView(APIView):

    """
        Adiantamento de parcelas do financiamento,
        com corpo da requisição:
         `{
            "number_of_installments": "int",
            "loan_id": "string"
        }`
    """

    def post(self, request, format=None):

        loan = RealStateLoan.active.filter(id=request.data['loan_id'])
        if loan.exists():
            loan = loan.first()
            if loan.installments_payed + request.data['number_of_installments'] > loan.number_of_installments :
                return Response({'error':'O número de parcelas adiantadas é maior que o restante'},400)

            loan.installments_payed = loan.installments_payed + request.data['number_of_installments']
            loan.save()

            status_code = 200
            data = {
                'loan_id': request.data['loan_id'],
                'number_of_installments_payed': loan.installments_payed
            }
        else:
            status_code = 404
            data = {'error':'Não encontrado o emprestimo'}

        return Response(data,status_code)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateLoanStatusView(APIView):

    """
        Status do financiamento imobiliario
    """

    def get(self, request, loan_id, format=None):

        loan = RealStateLoan.active.filter(id=loan_id)
        if loan.exists():
            status_code = 200
            data  = RealStateLoanSerializer(instance=loan.first()).data
        else:
            status_code = 404
            data = {"info":"Não encontrado o financiamento"}


        return Response(data,status_code)

    @classmethod
    def get_extra_actions(cls):
        return []

class RealStateFeeView(APIView):

    """
        Definição da taxa anual percentual de juros,
        com corpo da requisição:
        `{
            "fee_percent": "float"
        }`
    """

    def post(self, request, format=None):

        serializer = FeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #deactivate the old tax
        for obj in Fee.active.all():
            if obj.id == serializer.instance.id:
                continue
            obj.active = None
            obj.save()

        # send to log
        LogService().send_log(
            {
                "timestamp" : str(time.time()),
                "level" : "INFO",
                "microservice" : "ms-realstate-financing",
                "thread" : "main",
                "class" : self.__class__.__name__,
                "method" : "info",
                "message" : "Nova taxa de juros definida",
                "context" : "default",
                "ip" : IpService.get_my_ip()

            })

        return Response(serializer.data,200)

    @classmethod
    def get_extra_actions(cls):
        return []