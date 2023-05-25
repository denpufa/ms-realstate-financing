# Microservico: Real State Loan

## Financiamento Imobiliario:

*Endpoints (Financiamento Imobiliario):*
| Endpoint |Método http | Descrição |
| -------- | ----- | --------- |
| loan/real-state/v1/simulation | POST | Solicitar simulação recebendo valores de parcela, quantidade de parcelas, valor total a ser pago, juros ao anos, apartir dos dados de valor de entrada, total do imovel, renda mensal. |
| loan/real-state/v1/ | POST | Solicitar um financiamento imobiliario com valor de entrada, valor total do imovel, renda mensal |
| loan/real-state/financial-deferment/ | POST | Solicitar pagamento adiantado de parcelas |
| loan/real-state/v1/status | GET | Atualizar status corrente do empréstimo |
| loan/real-state/v1/fee | POST | Definir a taxa de juros praticada |


### Casos de uso: Finaciamento imobiliario

- O usuário pode simular um empréstimo;

- O usuário pode solicitar um empréstimo;

- O usuário pode solicitar pagar parcelas adiantandas;

- O usuário pode solicitar o status do empréstimo;

- O sistema deve recusar o a solicitação de empréstimo caso ela some mais de 30%
 da renda;

- O sistema caso aprovação deve solicitar o sistema de pagamento;

- O sistema deve adicionar 10% a mais de juros , caso a o empréstimo comprometa 25% da renda do usuário, por  causa do risco de credito;

- O sistema deve definir como 30% de desconto nos juros para parcelas pagas adiantadas;

- Definir taxa de juros;