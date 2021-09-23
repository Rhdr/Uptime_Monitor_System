from django.shortcuts import render
from .models import Website


# Views
def home(request):
    websites = Website.objects.order_by('site_name')

    #add row number
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1
        print(website, website.row_number)
    context_dict = {'websites': websites}

    return render(request, 'monitor/home.html', context_dict)