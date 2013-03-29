from django.contrib import admin
from webapp.models import Balance, Group, BudgetUserGroup, BudgetUser, PoliticalBranch, Programme, Category, Item

admin.site.register(Balance)
admin.site.register(Group)
admin.site.register(BudgetUserGroup)
admin.site.register(BudgetUser)
admin.site.register(PoliticalBranch)
admin.site.register(Programme)
admin.site.register(Category)
admin.site.register(Item)
