from rest_framework.views import APIView
from ..services.reports import Resume


class BasicResumView(APIView):
    """
        View dedicated to return a basic resume from the transactions
    """

    def get(self,request):
        return Resume().basic_resume()

class ByMonthResumView(APIView):
    """
        View dedicated to return a resume from the transactions by month
    """

    def get(self,request):
        return Resume().per_month()