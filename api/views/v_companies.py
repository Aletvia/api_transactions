from rest_framework.views import APIView
from ..services.reports import Resume


class CompanyResumView(APIView):
    """
        View dedicated to return a basic resume from the transactions
    """

    def get(self, request, code):
        return Resume().per_company(code)
