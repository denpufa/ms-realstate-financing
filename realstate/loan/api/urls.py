from django.urls import path, include
from rest_framework import routers
from .viewsets import (SimulationRealStateLoanView,
                       RealStateFeeView,
                       FinancialDefermentView,
                       RealStateLoanStatusView,
                       RealStateLoanView
                       )
urlpatterns = [

    path('simulation/',SimulationRealStateLoanView.as_view()),
    path('',RealStateLoanView.as_view()),
    path('financial-deferment/',FinancialDefermentView.as_view()),
    path('status/<str:loan_id>/',RealStateLoanStatusView.as_view()),
    path('fee/',RealStateFeeView.as_view())

]
