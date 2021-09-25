from django.shortcuts import render
from .extras.job_scheduler import JobScheduler
from .extras.slackbot import SlackBot
from .extras.url_inspect import Inspector
from .forms import WebsiteAddUpdateForm
from .models import Website


# Views
def home(request):
    # # # start website inspections & update db
    # job_scheduler = JobScheduler()
    # #slackbot = SlackBot()
    # slackbot = None
    # inspector = Inspector(job_scheduler, slackbot)
    # inspector.start_scheduled_inspection()

    update_form = WebsiteAddUpdateForm()

    #add row number
    websites = Website.objects.order_by('site_name')
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1

    if request.method == 'POST':
        add_form = WebsiteAddUpdateForm(request.POST)
        print("SiteName", add_form.cleaned_data['site_name'])
        if add_form.is_valid():
            add_form.save(commit=True)
    else:
        add_form = WebsiteAddUpdateForm()

    context_dict = {
        'websites': websites,
        'add_form': add_form,
        'update_form': update_form
    }
    return render(request, 'monitor/home.html', context_dict)