from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from .extras.job_scheduler import JobScheduler
from .extras.slackbot import SlackBot
from .extras.url_inspect import Inspector
from .forms import WebsiteAddUpdateForm
from .models import Website

job_scheduler = JobScheduler()
slackbot = SlackBot()
#slackbot = None
inspector = Inspector(job_scheduler, slackbot)


# Views
def home(request):
    # start website inspections & update db
    inspector.start_scheduled_inspection()

    #add row number
    websites = Website.objects.order_by('site_name')
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1

    context_dict = {
        'websites': websites,
    }
    return render(request, 'monitor/home.html', context_dict)


def ajax_json(request):
    websites = Website.objects.order_by('site_name')
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1
    return JsonResponse({"websites": list(websites.values())})


def ajax_create(request):
    if request.method == "POST":
        site_name = request.POST['site_name']
        site_url = request.POST['site_url']
        slack_token = request.POST['slack_token']
        slack_channel = request.POST['slack_channel']
        new_website = Website(site_name=site_name,
                              site_url=site_url,
                              slack_token=slack_token,
                              slack_channel=slack_channel)
        new_website.save()
        inspector.add_newly_created_website(new_website)
    return HttpResponse("New website created")


def ajax_edit(request):
    if request.method == "POST":
        pk_website = request.POST['pk_website']
        site_name = request.POST['site_name']
        site_url = request.POST['site_url']
        slack_token = request.POST['slack_token']
        slack_channel = request.POST['slack_channel']
        existing_website = Website.objects.get(pk_website=pk_website)
        existing_website.site_name = site_name
        existing_website.site_url = site_url
        existing_website.slack_token = slack_token
        existing_website.slack_channel = slack_channel
        existing_website.save()
    return HttpResponse("Website edited")


def ajax_delete(request):
    if request.method == "POST":
        pk_website = request.POST['pk_website']
        existing_website = Website.objects.get(pk_website=pk_website)
        existing_website.delete()
        inspector.remove_website(existing_website)
    return HttpResponse("Website deleted")
