from django.urls import path
from api.views.v_transactions import BasicResumView

urlpatterns = [
   path('resume',
         BasicResumView.as_view(),
         name='resume_view'),
]