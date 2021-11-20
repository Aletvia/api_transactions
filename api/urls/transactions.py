from django.urls import path
from api.views.v_transactions import BasicResumView, ByMonthResumView

urlpatterns = [
   path('resume',
         BasicResumView.as_view(),
         name='resume_view'),
   path('resume/month',
         ByMonthResumView.as_view(),
         name='resume_by_month_view'),
]