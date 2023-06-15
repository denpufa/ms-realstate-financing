from rest_framework.test import APITestCase, APIClient
from loan.models import RealStateLoan

class LoanRealStateTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        RealStateLoan.objects.create(
            real_state_total_value = 100000.00,
            entry_value = 1000.00,
            loan_total_value = 150000.00,
            monthly_income = 10000.00,
            number_of_installments = 120,
            user_id = '11bt7hkkffu677',
            interest_rate_per_year = 10.0,
            value_per_month = 2500.00
        )

    def test_post_fee(self):

        client = APIClient()
        response = client.post('/loan/real-state/v1/fee/',data={
            'fee_per_year': 12.0
        },format='json')

        self.assertEqual(response.status_code, 200)

    def test_loan_simulation(self):

        client = APIClient()

        response = client.post('/loan/real-state/v1/simulation/',data={
            "real_state_total_value": 1000.00,
            "entry_value" : 100.00,
            "monthly_income" : 3000.00,
            "number_of_installments": 12
            },headers={'user_id':'ab29msm23o4bok2k3'},format='json')

        self.assertEqual(response.status_code, 200)

    def test_loan_real_state(self):

        client = APIClient()

        response = client.post('/loan/real-state/v1/',data={
            "real_state_total_value": 1000.00,
            "entry_value" : 100.00,
            "monthly_income" : 3000.00,
            "number_of_installments": 12
            },headers={'user_id':'ab29msm23o4bok2k3'},format='json')

        self.assertEqual(response.status_code, 200)

    def test_loan_status(self):

        client = APIClient()
        id = RealStateLoan.objects.first().id

        response = client.get(f'/loan/real-state/v1/status/{id}/',format='json')

        self.assertEqual(response.status_code, 200)

    def test_financial_deferment(self):

        client = APIClient()
        id = RealStateLoan.objects.first().id

        response = client.post('/loan/real-state/v1/financial-deferment/',
                               data={'loan_id':str(id),
                                     'number_of_installments':2
                                    }
                               ,format='json')

        self.assertEqual(response.status_code, 200)



