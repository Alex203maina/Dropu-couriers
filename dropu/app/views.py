from django.shortcuts import render
from .models import Services, FeatureSection, Feature, FactSection
from django.shortcuts import render, get_object_or_404
from .models import LogisticsPrice
from .forms import LogisticsSearchForm
from django.db.models import Q

# Create your views here.
def index(request):
    services = Services.objects.all().order_by('service_title')[:3]
    feature_section = FeatureSection.objects.first()
    features = Feature.objects.all()
    fact_section = FactSection.objects.prefetch_related('fact_boxes').first()
    return render(request, 'index.html', {"services": services,
                                        "feature_section": feature_section, 
                                        "features": features,
                                        "fact_section": fact_section
                                        })

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'feature.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def search_price(request):
    result = None
    if request.method == 'POST':
        form = LogisticsSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            # Perform a case-insensitive partial match
            result = LogisticsPrice.objects.filter(location__icontains=location)
    else:
        form = LogisticsSearchForm()

    return render(request, 'search.html', {'form': form, 'result': result})