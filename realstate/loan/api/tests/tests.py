from rest_framework.test import APITestCase, APIClient

class LoanRealStateTestCase(APITestCase):

    def test_loan_simulation(self):

        client = APIClient()

        response = client.post('/loan/real-state/v1/',data={
            "user_id" : "string",
            "real_state_total_value": 1000.00,
            "entry_value" : 100.00,
            "monthly_income" : 3000.00,
            "number_of_installments": 12
            },format='json')

