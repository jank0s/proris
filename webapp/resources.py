# webapp/api.py
from tastypie.resources import ModelResource
from webapp.models import Group, BudgetUserGroup, BudgetUser, Balance, PoliticalBranch, Programme, Category, Item
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django.db.models import Avg, Max, Min, Count, Sum
import sys

class BalanceResource(ModelResource):
    categories = fields.ToManyField('webapp.resources.CategoryResource', 'categories')
    class Meta:
        queryset = Balance.objects.all()
        resource_name = "balance"
        filtering = {
            'categories': ALL_WITH_RELATIONS,
            }

class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = "group"

class BudgerUserGroupResource(ModelResource):
    group = fields.ForeignKey(GroupResource, 'group')
    class Meta:
        queryset = BudgetUserGroup.objects.all()
        resource_name = "bug"

class BudgetUserResource(ModelResource):
    categories = fields.ToManyField('webapp.resources.CategoryResource', 'categories')
    group = fields.ForeignKey(BudgerUserGroupResource, 'group')
    class Meta:
        queryset = BudgetUser.objects.all()
        resource_name = "bu"
        filtering = {
            'categories': ALL_WITH_RELATIONS,
            }

class PoliticalBranchResource(ModelResource):
    categories = fields.ToManyField('webapp.resources.CategoryResource', 'categories')
    class Meta:
        queryset = PoliticalBranch.objects.all()
        resource_name = "pb"
        filtering = {
            'categories': ALL_WITH_RELATIONS,
            }
        
class ProgrammeResource(ModelResource):
    categories = fields.ToManyField('webapp.resources.CategoryResource', 'categories')
    class Meta:
        queryset = Programme.objects.all()
        resource_name = "programme"
        filtering = {
            'categories': ALL_WITH_RELATIONS,
            }

class CategoryResource(ModelResource):
    balance = fields.ForeignKey(BalanceResource, 'balance')
    budget_user = fields.ForeignKey(BudgetUserResource, 'budget_user')
    political_branch = fields.ForeignKey(PoliticalBranchResource, 'political_branch')
    programme = fields.ForeignKey(ProgrammeResource, 'programme')
    items = fields.ToManyField('webapp.resources.ItemResource', 'items')
    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"
        filtering = {
            'items': ALL_WITH_RELATIONS,
            }

class ItemResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')
    class Meta:
        queryset = Item.objects.all()
        resource_name = "item"
        filtering = {
            'budget_year': ALL,
            'category': ALL_WITH_RELATIONS,
            }
