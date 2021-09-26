from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .extras.job_scheduler import JobScheduler
from .extras.slackbot import SlackBot
from .extras.url_inspect import Inspector
from .forms import WebsiteAddUpdateForm
from .models import Website

job_scheduler = JobScheduler()
#slackbot = SlackBot()
slackbot = None
inspector = Inspector(job_scheduler, slackbot)


# Views
def home(request, edit_obj=None):
    # start website inspections & update db
    #inspector.start_scheduled_inspection()

    #add row number
    websites = Website.objects.order_by('site_name')
    for row_number, website in enumerate(websites):
        website.row_number = row_number + 1

    if request.method == 'POST':
        if edit_obj:
            print("Edit obj:", edit_obj)
            add_form = WebsiteAddUpdateForm(request.POST, instance=edit_obj)
        else:
            print("Add obj")
            add_form = WebsiteAddUpdateForm(request.POST)
        if add_form.is_valid():
            #print("SiteName", add_form.cleaned_data['site_name'])
            add_form.save(commit=True)
    else:
        if edit_obj:
            print("Edit obj:", edit_obj)
            add_form = WebsiteAddUpdateForm(instance=edit_obj)
        else:
            print("Add obj")
            add_form = WebsiteAddUpdateForm()

    context_dict = {
        'websites': websites,
        'add_form': add_form,
    }
    return render(request, 'monitor/home.html', context_dict)


def home_add(request):
    return home(request)


def home_edit(request, pk):
    website = Website.objects.get(pk=pk)
    return home(request, website)


def home_delete(request, pk):
    print("DELETING")
    website = Website.objects.get(pk=pk)
    website.delete()
    website.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))