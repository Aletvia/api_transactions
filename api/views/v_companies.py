from rest_framework.views import APIView
from ..services.reports import Resume


class CompanyResumView(APIView):
    """
        View dedicated to return a resume from the transactions of a company
    """

    def get(self, request, code):
        return Resume().per_company(code)


class CompanyVSCompanyApprovedResumView(APIView):
    """
        View dedicated to return a resume from the transactions approved by company
    """

    def get(self, request):
        return Resume().company_vs_company_transactions_approved()


class CompanyVSCompanyRejectedResumView(APIView):
    """
        View dedicated to return a resume from the transactions rejected by company
    """

    def get(self, request):
        return Resume().company_vs_company_transactions_rejected()