from django.shortcuts import render
from .extras.job_scheduler import JobScheduler
from .extras.slackbot import SlackBot
from .extras.url_inspect import Inspector
from .models import Website


# Views
def home(request):
    # start website inspections & update db
    job_scheduler = JobScheduler()
    #slackbot = SlackBot()
    slackbot = None
    inspector = Inspector(job_scheduler, slackbot)
    inspector.start_scheduled_inspection()

    #add row number
    websites = Website.objects.order_by('site_name')
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1
    context_dict = {'websites': websites}

    return render(request, 'monitor/home.html', context_dict)