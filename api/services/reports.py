from django.db.models import Count, Max, Sum, FloatField, Avg
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.db.models import Q
from api.models.company import Company
from rest_framework import status


from api.models.transaction import Transaction

class Resume:
    closed = Q(transaction_status='c')
    reversed = Q(transaction_status='r')
    charged_t = Q(charged=True)
    charged_f = Q(charged=False)
    active_companies = Q(company__active=True)

    def basic_resume(self):
        """
        Resume of the transactions with the next data:
            - Company with more transactions approved
            - Company with less transactions approved
            - Company with less transactions rejected
            - Company with more transactions rejected
            - Amount collected from all transactions approved
            - Amount lost from all transactions rejected
        """
        try:
            transactions_active_closed = Transaction.objects.filter(self.active_companies & self.closed)
            transactions_collected = transactions_active_closed.filter(self.charged_t)
            transactions_rejected = transactions_active_closed.filter(self.charged_f)

            num_sales_by_company = transactions_collected.select_related('company').values('company__name').annotate(number_of_sales=Count('folio')).order_by('number_of_sales')
            amount_collected = transactions_collected.annotate(as_float=Cast('price', FloatField())).aggregate(amount=Sum('as_float'))

            num_rejections_by_company = transactions_rejected.select_related('company').values('company__name').annotate(number_of_sales=Count('folio')).order_by('number_of_sales')
            amount_lost = transactions_rejected.annotate(as_float=Cast('price', FloatField())).aggregate(amount=Sum('as_float'))

            report={
                'companies':{
                    'best_in_sales':num_sales_by_company.first(),
                    'worst_in_sales':num_sales_by_company.last(),
                    'with_less_rejections':num_rejections_by_company.first(),
                    'with_more_rejections':num_rejections_by_company.last()
                },
                'amounts':{
                    'collected':amount_collected['amount'],
                    'rejected':amount_lost['amount']
                }
            }
            return JsonResponse(report,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error':"Something went bad, try again later"}, status=status.HTTP_400_BAD_REQUEST)

    def per_company(self,company_code):
        """
        Resume of the company with the next data:
            - General information {name, if is active}
            - From all it transactions:
                - Number of transactions approved
                - Number of transactions rejected
                - Amount collected from all transactions approved
                - Amount lost from all transactions rejected
                - Average daily amount collected from all transactions approved
                - Day with best amount collected {day, amount collected, number of transactions}
        """
        try:
            company= Company.objects.get(code=company_code)
            id_ = Q(company__pk=company.pk)
            transactions_of_id=Transaction.objects.filter(id_ & self.closed).annotate(as_float=Cast('price', FloatField()))
            approved = transactions_of_id.filter(self.charged_t)

            rejected = transactions_of_id.filter(self.charged_f).aggregate(amount=Sum('as_float'),number=Count('price'))
            collected = approved.aggregate(amount=Sum('as_float'),number=Count('price'))
            by_day = approved.values('date__date').annotate(number=Count('date__date'),total=Sum('as_float'))
            average = by_day.aggregate(avg=Avg('total'))
            max = by_day.aggregate(goal=Max('total'))
            better_day = by_day.filter(total=max['goal'])
            ave_2 =round(average['avg'],1)
            report={
                'general':{
                    'name':company.name,
                    'active':company.active,
                },
                'transactions':{
                    'approved':collected['number'],
                    'rejected':rejected['number'],
                },
                'amounts':{
                    'collected':collected['amount'],
                    'lost':rejected['amount'],
                    'daily_average':ave_2,
                },
                'better_day':{
                    'date':better_day[0]['date__date'].strftime("%m-%d-%Y"),
                    'transactions':better_day[0]['number'],
                    'collected':better_day[0]['total']
                }
            }
            return JsonResponse(report,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error':"Something went bad, try again later"}, status=status.HTTP_400_BAD_REQUEST)

    def per_month(self):
        """
        Resume of the transactions per month with the next data:
            - Number of month
            - Number of transactions in the month
            - Amount collected in the month
        """
        try:
            transactions_active_closed = Transaction.objects.filter(self.active_companies & self.closed).annotate(as_float=Cast('price', FloatField()))
            transactions_collected = transactions_active_closed.filter(self.charged_t)
            transactions_rejected = transactions_active_closed.filter(self.charged_f)

            by_day = transactions_collected.values('date__month').annotate(number_of_transactions=Count('date__month'),amount_collected=Sum('as_float')).order_by('date__month')
            print(by_day)
            data = list(by_day)
            return JsonResponse(data,safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error':"Something went bad, try again later"}, status=status.HTTP_400_BAD_REQUEST)

    def company_vs_company_transactions_approved(self):
        """
        Resume of the transactions approved per company with the next data:
            - Name of company
            - Number of transactions approved
            - Amount collected in the month
        """
        try:
            transactions_active_closed = Transaction.objects.filter(self.active_companies & self.closed).annotate(as_float=Cast('price', FloatField())).select_related('company').values('company__name')
            transactions_collected = transactions_active_closed.filter(self.charged_t)

            approved_by_company = transactions_collected.annotate(number_of_sales=Count('folio'),amount_collected=Sum('as_float')).order_by('company__name')
            return JsonResponse(list(approved_by_company),safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error':"Something went bad, try again later"}, status=status.HTTP_400_BAD_REQUEST)

    
    def company_vs_company_transactions_rejected(self):
        """
        Resume of the transactions rejected per company with the next data:
            - Name of company
            - Number of transactions rejected
            - Amount collected in the month
        """
        try:
            transactions_active_closed = Transaction.objects.filter(self.active_companies & self.closed).annotate(as_float=Cast('price', FloatField())).select_related('company').values('company__name')
            transactions_rejected = transactions_active_closed.filter(self.charged_f)

            rejected_by_company = transactions_rejected.annotate(number_of_rejections=Count('folio'),amount_lost=Sum('as_float')).order_by('company__name')
            return JsonResponse(list(rejected_by_company),safe=False,status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'Error':"Something went bad, try again later"}, status=status.HTTP_400_BAD_REQUEST)