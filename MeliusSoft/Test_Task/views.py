from django.shortcuts import render
from .models import *

def index(request):
    if request.method == 'POST':
        manufacturers = []
        credit_applications = CreditApplicationModel.objects.filter(contract_id=request.POST.get('id'))
        products = ProductModel.objects.prefetch_related('manufacturer').filter(credit_application_id__in=list(credit_applications))
        for product in products:
            if product.manufacturer not in manufacturers:
                manufacturers.append(product.manufacturer)
        context = {'manufacturers':manufacturers}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
