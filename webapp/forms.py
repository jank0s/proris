from django import forms
from webapp.models import Balance, Group, BudgetUserGroup, BudgetUser, PoliticalBranch, Programme, Category, Item
import csv

class DataInput(forms.Form):
    file = forms.FileField()
    
    def save(self):
        records = csv.reader(self.cleaned_data["file"], delimiter=';')
         
        for line in records:     
            if not Balance.objects.filter(name=line[1]).exists():
                idata = Balance()
                idata.name = line[1]
                idata.save()
            key = Balance.objects.filter(name=line[1]).get().pk
                
            if not Group.objects.filter(name=line[3]).filter(balance=key).exists():
                idata = Balance.objects.get(pk=key)
                idata.group_set.create(name=line[3])
            key = Group.objects.filter(name=line[3]).filter(balance=key).get().pk
                
            if not BudgetUserGroup.objects.filter(name=line[5]).filter(group=key).exists():
                idata = Group.objects.get(pk=key)
                idata.budgetusergroup_set.create(name=line[5])
            key = BudgetUserGroup.objects.filter(name=line[5]).filter(group=key).get().pk
                
            if not BudgetUser.objects.filter(name=line[7]).filter(group=key).exists():
                idata = BudgetUserGroup.objects.get(pk=key)
                idata.budgetuser_set.create(name=line[7])
            key = BudgetUser.objects.filter(name=line[7]).filter(group=key).get().pk    
                
            if not PoliticalBranch.objects.filter(name=line[9]).filter(budget_user=key).exists():
                idata = BudgetUser.objects.get(pk=key)
                idata.politicalbranch_set.create(name=line[9])
            key = PoliticalBranch.objects.filter(name=line[9]).filter(budget_user=key).get().pk
            
            if not Programme.objects.filter(name=line[11]).filter(political_branch=key).exists():
                idata = PoliticalBranch.objects.get(pk=key)
                idata.programme_set.create(name=line[11])
            key = Programme.objects.filter(name=line[11]).filter(political_branch=key).get().pk
            
            if not Category.objects.filter(name=line[13]).filter(programme=key).exists():
                idata = Programme.objects.get(pk=key)
                idata.category_set.create(name=line[13])
            key = Category.objects.filter(name=line[13]).filter(programme=key).get().pk
            
                