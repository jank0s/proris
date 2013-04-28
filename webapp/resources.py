# webapp/api.py
from tastypie.resources import ModelResource
from webapp.models import Group, BudgetUserGroup, BudgetUser, Balance, PoliticalBranch, Programme, Category, Item
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class BalanceResource(ModelResource):
    class Meta:
        queryset = Balance.objects.all()
        resource_name = "balance"


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
    group = fields.ForeignKey(BudgerUserGroupResource, 'group')
    class Meta:
        queryset = BudgetUserGroup.objects.all()
        resource_name = "bu"

class PoliticalBranchResource(ModelResource):
    class Meta:
        queryset = PoliticalBranch.objects.all()
        resource_name = "pb"

class ProgrammeResource(ModelResource):
    class Meta:
        queryset = Programme.objects.all()
        resource_name = "programme"

class CategoryResource(ModelResource):
    balance = fields.ForeignKey(BalanceResource, 'balance')
    budget_user = fields.ForeignKey(BudgetUserResource, 'budget_user')
    political_branch = fields.ForeignKey(PoliticalBranchResource, 'political_branch')
    programme = fields.ForeignKey(ProgrammeResource, 'programme')
    class Meta:
        queryset = Category.objects.all()
        resource_name = "category"

class ItemResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')
    filtering = {
        "budget_year": ALL,
        }
    class Meta:
        queryset = Item.objects.all()
        resource_name = "item"
