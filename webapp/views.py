from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response, render
from webapp.forms import DataInput
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages
from webapp.models import BudgetUserGroup, BudgetUser, PoliticalBranch, Item
from django.db.models import Sum
import json


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
                messages.error(request, "Something went wrong. Please check if you uploaded the correct"
                                        " file and that it is encoded in the correct format (UTF-8)")
        else:
            context = {"form": form}
    else:
        form = DataInput()
        context = {"form": form}

    return render_to_response("admin/import_csv.html", context,
                              context_instance=RequestContext(request))


def index(request):
    return render(request, 'webapp/index.html')

def year(request):
    #query
    query = Item.objects.values('budget_year').distinct()
    #prepare data
    data = [{'year': q['budget_year']} for q in query]
    return HttpResponse(json.dumps(data), mimetype='application/json')

def pb(request, year):
    #calculate sum
    sum = Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
    #query
    branch_list = PoliticalBranch.objects.values('name').filter(categories__items__budget_year=year)
    branch_list = branch_list.annotate(branch_sum=Sum('categories__items__value'))
    branch_list = branch_list.values('id', 'name', 'branch_sum').order_by('-branch_sum')
    #reference year
    if (Item.objects.values('budget_year').distinct().filter(budget_year=(int(year)-1)).exists()):
        ref_year=int(year)-1
    else:
        ref_year=year
    #ref_data
    ref = PoliticalBranch.objects.values('name').filter(categories__items__budget_year=ref_year)
    ref = ref.annotate(branch_sum=Sum('categories__items__value'))
    ref = ref.values('id', 'branch_sum')
    #calculate percentage
    list = [{'id': br['id'], 'name': br['name'], 'value': br['branch_sum'], 'percent': br['branch_sum']/sum*100,
             'ref': ((ref.get(id=br['id']).get('branch_sum'))-br['branch_sum'])/br['branch_sum']}
            for br in branch_list]
    #prepare data
    data = {'list':list, 'sum':sum}
    #return json
    return HttpResponse(json.dumps(data), mimetype='application/json')

def pb_item(request, year, pb_id):
    #calculate sum
    sum = Item.objects.filter(budget_year=year).filter(category__political_branch_id=pb_id)
    sum = sum.aggregate(s=Sum('value'))['s']
    #query
    item_list = Item.objects.filter(budget_year=year).filter(category__political_branch_id=pb_id)
    item_list = item_list.values('category__name').annotate(item_sum=Sum('value')).order_by().order_by("-item_sum")
    #reference year
    if (Item.objects.values('budget_year').distinct().filter(budget_year=(int(year)-1)).exists()):
        ref_year=int(year)-1
    else:
        ref_year=year
    #ref_data
    ref = Item.objects.filter(budget_year=ref_year).filter(category__political_branch_id=pb_id)
    ref = ref.values('category__name').annotate(item_sum=Sum('value')).order_by()
    ref = ref.values('category__name', 'item_sum')
    #calculate percentage
    list = [{'name': item['category__name'], 'value': item['item_sum'], 'percent': item['item_sum']/sum*100,
             'ref': ((ref.get(category__name=item['category__name']).get('item_sum'))-item['item_sum'])/item['item_sum']}
            for item in item_list]
    #refernce sums
    ref_list = Item.objects.values('budget_year').filter(category__political_branch_id=pb_id)
    ref_list.group_by=['budget_year']
    ref_list = ref_list.annotate(item_sum=Sum('value'))
    rf_list = [{'year': rf['budget_year'], 'value': rf['item_sum']}
            for rf in ref_list]
    #prepare data
    data = {'list': list, 'sum': sum, 'name': PoliticalBranch.objects.get(pk=pb_id).name, 'ref': rf_list}
    #return json
    return HttpResponse(json.dumps(data), mimetype='application/json')


def bug(request, year):
    #calculate sum
    sum = Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
    #query
    bug_list = BudgetUserGroup.objects.values('name').filter(budgetuser__categories__items__budget_year=year)
    bug_list = bug_list.annotate(group_sum=Sum('budgetuser__categories__items__value'))
    bug_list = bug_list.values('id', 'name', 'group_sum').order_by('-group_sum')
    #reference year
    if (Item.objects.values('budget_year').distinct().filter(budget_year=(int(year)-1)).exists()):
        ref_year=int(year)-1
    else:
        ref_year=year
        #ref_data
    ref = BudgetUserGroup.objects.values('name').filter(budgetuser__categories__items__budget_year=ref_year)
    ref = ref.annotate(group_sum=Sum('budgetuser__categories__items__value'))
    ref = ref.values('id', 'group_sum')
    #calculate percentage
    list = [{'id': br['id'], 'name': br['name'], 'value': br['group_sum'], 'percent': br['group_sum']/sum*100,
             'ref': ((ref.get(id=br['id']).get('group_sum'))-br['group_sum'])/br['group_sum']}
            for br in bug_list]
    #prepare data
    data = {'list':list, 'sum':sum}
    #return json
    return HttpResponse(json.dumps(data), mimetype='application/json')


def bug_bu(request, year, bug_id):
    #calculate sum
    sum = Item.objects.filter(budget_year=year).filter(category__budget_user__group__id=bug_id)
    sum = sum.aggregate(s=Sum('value'))['s']
    #query
    bug_list = BudgetUser.objects.values('name').filter(categories__items__budget_year=year).filter(group__id=bug_id)
    bug_list = bug_list.annotate(group_sum=Sum('categories__items__value'))
    bug_list = bug_list.values('id', 'name', 'group_sum').order_by('-group_sum')
    #reference year
    if (Item.objects.values('budget_year').distinct().filter(budget_year=(int(year)-1)).exists()):
        ref_year=int(year)-1
    else:
        ref_year=year
        #ref_data
    ref = BudgetUser.objects.values('name').filter(categories__items__budget_year=ref_year).filter(group__id=bug_id)
    ref = ref.annotate(group_sum=Sum('categories__items__value'))
    ref = ref.values('id', 'group_sum')
    #calculate percentage
    list = [{'id': br['id'], 'name': br['name'], 'value': br['group_sum'], 'percent': br['group_sum']/sum*100,
             'ref': ((ref.get(id=br['id']).get('group_sum'))-br['group_sum'])/br['group_sum']}
            for br in bug_list]
    #refernce sums
    ref_list = Item.objects.values('budget_year').filter(category__budget_user__group__id=bug_id)
    ref_list.group_by=['budget_year']
    ref_list = ref_list.annotate(item_sum=Sum('value'))
    rf_list = [{'year': rf['budget_year'], 'value': rf['item_sum']}
               for rf in ref_list]
    #prepare data
    data = {'list': list, 'sum': sum, 'name': BudgetUserGroup.objects.get(pk=bug_id).name, 'ref': rf_list}
    #return json
    return HttpResponse(json.dumps(data), mimetype='application/json')


def bug_bu_item(request, year, bug_id, bu_id):
    #calculate sum
    sum = Item.objects.filter(budget_year=year).filter(category__budget_user__group__id=bug_id)
    sum = sum.filter(category__budget_user_id=bu_id).aggregate(s=Sum('value'))['s']
    #query
    item_list = Item.objects.filter(budget_year=year).filter(category__budget_user_id=bu_id)
    item_list = item_list.filter(category__budget_user__group_id=bug_id)
    item_list = item_list.values('category__id', 'id', 'category__name', 'value').order_by('-value')
    #reference year
    if (Item.objects.values('budget_year').distinct().filter(budget_year=(int(year)-1)).exists()):
        ref_year=int(year)-1
    else:
        ref_year=year
    #ref_data
    ref = Item.objects.filter(budget_year=ref_year).filter(category__budget_user_id=bu_id)
    ref = ref.filter(category__budget_user__group_id=bug_id)
    ref = ref.values('category__id', 'value')
    #calculate percentage
    list = [{'id': "", 'name': item['category__name'], 'value': item['value'], 'percent': item['value']/sum*100,
             'ref': ((ref.get(category__id=item['category__id']).get('value'))-item['value'])/item['value']}
            for item in item_list]
    #refernce sums
    ref_list = Item.objects.values('budget_year').filter(category__budget_user__group__id=bug_id)
    ref_list = ref_list.filter(category__budget_user_id=bu_id)
    ref_list.group_by=['budget_year']
    ref_list = ref_list.annotate(item_sum=Sum('value'))
    rf_list = [{'year': rf['budget_year'], 'value': rf['item_sum']}
               for rf in ref_list]
    #prepare data
    bug_name = BudgetUserGroup.objects.get(pk=bug_id).name
    name  = BudgetUser.objects.get(pk=bu_id).name
    data = {'list': list, 'sum': sum, 'bug_name': bug_name , 'name': name, 'ref': rf_list}
    #return json
    return HttpResponse(json.dumps(data), mimetype='application/json')
