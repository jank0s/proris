from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from webapp.forms import DataInput
from django.template import RequestContext
from django.http import HttpResponse
from webapp.models import Group, BudgetUserGroup, BudgetUser, Balance, PoliticalBranch, Programme, Category, Item


@staff_member_required
def importcsv(request):
    if request.method == "POST":
        form = DataInput(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("%s" % form.is_valid())
    else:
        form = DataInput()
        context = {"form": form}
        return render_to_response("import_csv.html", context,
        context_instance=RequestContext(request))

def index(request):
    latest_poll_list = PoliticalBranch.objects.all()
    output = '</br>'.join([p.name for p in latest_poll_list])
    return HttpResponse(output)