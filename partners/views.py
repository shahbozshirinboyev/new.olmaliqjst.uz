from django.shortcuts import render

from .models import PartnerCategory


def partner_list(request):
    categories = PartnerCategory.objects.prefetch_related('partners').all()
    return render(request, 'partners/partner_list.html', {'categories': categories})