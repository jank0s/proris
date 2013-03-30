from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response, render
from webapp.forms import DataInput
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages
from webapp.models import Group, BudgetUserGroup, BudgetUser, Balance, PoliticalBranch, Programme, Category, Item
from django.db.models import Avg, Max, Min, Count, Sum


@staff_member_required
def importcsv(request):
    if request.method == "POST":
        form = DataInput(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                context = {"form": form}
                messages.success(request, "Import was successful")
            except:
                context = {"form": form}
                messages.error(request, "Something went wrong. Please check if you uploaded the correct file and that it is encoded in the correct format (UTF-8)")
        else:
            context = {"form": form}
    else:
        form = DataInput()
        context = {"form": form}
        
    return render_to_response("admin/import_csv.html", context,
                                          context_instance=RequestContext(request))


def index(request):
    branch_list = PoliticalBranch.objects.annotate(sum=Sum('category__item__value')).values('name', 'sum')
    context = {'branch_list': branch_list}
    return render(request, 'webapp/index.html', context)
