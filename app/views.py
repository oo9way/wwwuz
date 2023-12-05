from django.shortcuts import render
from app.models import Data
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    data = Data.objects.filter(date__gte=today).order_by('-unique_visitors')

    data = Paginator(data, 10)
    page = request.GET.get('page', 1)
    
    try:
        rows = data.page(page)
    except PageNotAnInteger:
        rows = data.page(1)
    except EmptyPage:
        rows = data.page(data.num_pages)
        
    return render(request, 'home.html', {'rows':rows})

