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
    path="Kategorije"
    header="Kategorije"
    sum=Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
    branch_list = PoliticalBranch.objects.values('name').filter(category__item__budget_year=year).annotate(branch_sum=Sum('category__item__value')).values('id', 'name', 'branch_sum').order_by('-branch_sum')
    branch_list = [{'id': br['id'], 'name': br['name'], 'branch_sum': br['branch_sum'], 'percent': br['branch_sum']/sum*100}
        for br in branch_list]
    context = {'branch_list': branch_list, 'path': path, 'header': header}
    return render(request, 'webapp/index.html', context)

def pb(request, year):
    path="Kategorije"
    header="Kategorije"
    sum=Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
    branch_list = PoliticalBranch.objects.values('name').filter(category__item__budget_year=year).annotate(branch_sum=Sum('category__item__value')).values('id', 'name', 'branch_sum').order_by('-branch_sum')
    list = [{'id': br['id'], 'name': br['name'], 'value': br['branch_sum'], 'percent': br['branch_sum']/sum*100}
                   for br in branch_list]
    context = {'list': list, 'path': path, 'header': header}
    return render(request, 'webapp/view.html', context)

def pb_item(request, year, pb_id):
    header="Kategorije"
    sum=Item.objects.filter(budget_year=year).filter(category__political_branch_id=pb_id).aggregate(s=Sum('value'))['s']
    item_list = Item.objects.filter(budget_year=year).filter(category__political_branch_id=pb_id).values('id', 'category__name', 'value').order_by('-value')
    list = [{'id': "", 'name': item['category__name'], 'value': item['value'], 'percent': item['value']/sum*100}
        for item in item_list]
    context = {'list': list, 'path': PoliticalBranch.objects.get(pk=pb_id).name, 'header': PoliticalBranch.objects.get(pk=pb_id).name}
    return render(request, 'webapp/view.html', context)

def bug(request, year):
    path="Skupine proracunskih uporabnikov"
    header="Skupine proracunskih uporabnikov"
    sum=Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
    bug_list = BudgetUserGroup.objects.values('name').filter(budgetuser__category__item__budget_year=year).annotate(group_sum=Sum('budgetuser__category__item__value')).values('id', 'name', 'group_sum').order_by('-group_sum')
    list = [{'id': br['id'], 'name': br['name'], 'value': br['group_sum'], 'percent': br['group_sum']/sum*100}
            for br in bug_list]
    context = {'list': list, 'path': path, 'header': header}
    return render(request, 'webapp/view.html', context)

def bug_bu(request, year, bug_id):
    sum=Item.objects.filter(budget_year=year).filter(category__budget_user__group__id=bug_id).aggregate(s=Sum('value'))['s']
    bug_list = BudgetUser.objects.values('name').filter(category__item__budget_year=year).filter(group__id=bug_id).annotate(group_sum=Sum('category__item__value')).values('id', 'name', 'group_sum').order_by('-group_sum')
    list = [{'id': br['id'], 'name': br['name'], 'value': br['group_sum'], 'percent': br['group_sum']/sum*100}
            for br in bug_list]
    context = {'list': list, 'path': BudgetUserGroup.objects.get(pk=bug_id).name, 'header': BudgetUserGroup.objects.get(pk=bug_id).name}
    return render(request, 'webapp/view.html', context)

def bug_bu_item(request, year, bug_id, bu_id):
    sum=Item.objects.filter(budget_year=year).filter(category__budget_user__group__id=bug_id).filter(category__budget_user_id=bu_id).aggregate(s=Sum('value'))['s']
    item_list = Item.objects.filter(budget_year=year).filter(category__budget_user_id=bu_id).filter(category__budget_user__group_id=bug_id).values('id', 'category__name', 'value').order_by('-value')
    list = [{'id': "", 'name': item['category__name'], 'value': item['value'], 'percent': item['value']/sum*100}
            for item in item_list]
    context = {'list': list, 'path': BudgetUser.objects.get(pk=bu_id).name, 'header': BudgetUser.objects.get(pk=bu_id)}
    return render(request, 'webapp/view.html', context)