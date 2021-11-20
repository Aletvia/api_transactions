from django.urls import path
from api.views.v_companies import CompanyResumView, CompanyVSCompanyApprovedResumView, CompanyVSCompanyRejectedResumView

urlpatterns = [
   path('resume/<int:code>',
         CompanyResumView.as_view(),
         name='company_resume_view'),
   path('storm/approved',
         CompanyVSCompanyApprovedResumView.as_view(),
         name='storm_approved_view'),
   path('storm/rejected',
         CompanyVSCompanyRejectedResumView.as_view(),
         name='storm_rejected_view'),
]