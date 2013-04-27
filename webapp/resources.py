# webapp/api.py
from tastypie.resources import ModelResource
from webapp.models import Group, BudgetUserGroup, BudgetUser, Balance, PoliticalBranch, Programme, Category, Item
from django.db.models import Avg, Max, Min, Count, Sum


class PBResource(ModelResource):
    class Meta:
        #calculate sum
        year=2013
        sum=Item.objects.filter(budget_year=year).aggregate(s=Sum('value'))['s']
        #query
        branch_list = PoliticalBranch.objects.values('name').filter(category__item__budget_year=year).annotate(branch_sum=Sum('category__item__value')).values('id', 'name', 'branch_sum').order_by('-branch_sum')
        #calculate percentage
        list = [{'id': br['id'], 'name': br['name'], 'value': br['branch_sum'], 'percent': br['branch_sum']/sum*100}
                for br in branch_list]
        queryset = PoliticalBranch.objects.all()
        resource_name = 'pb'

