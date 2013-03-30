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
    year=2013;
    sum=Item.objects.filter(budget_year="2013").aggregate(s=Sum('value'))['s']
    branch_list = PoliticalBranch.objects.values('name').filter(category__item__budget_year=year).annotate(branch_sum=Sum('category__item__value')).values('name', 'branch_sum').order_by('-branch_sum')
    branch_list = [{'name': br['name'], 'branch_sum': br['branch_sum'], 'percent': br['branch_sum']/sum*100}
        for br in branch_list]
    context = {'branch_list': branch_list}
    return render(request, 'webapp/index.html', context)
