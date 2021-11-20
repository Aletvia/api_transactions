from rest_framework.views import APIView
from ..services.reports import Resume


class CompanyResumView(APIView):
    """
        View dedicated to return a resume from the transactions of a company
    """

    def get(self, request, code):
        return Resume().per_company(code)
