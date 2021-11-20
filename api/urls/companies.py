from django.urls import path
from api.views.v_companies import CompanyResumView

urlpatterns = [
   path('resume/<int:code>',
         CompanyResumView.as_view(),
         name='company_resume_view'),
]