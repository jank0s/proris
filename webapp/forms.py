from django import forms
from webapp.models import Balance, Group, BudgetUserGroup, BudgetUser, PoliticalBranch, Programme, Category, Item
import csv

class DataInput(forms.Form):
    file = forms.FileField(help_text="*File must be encoded in UTF-8 format")
    year = forms.IntegerField()
    
    def save(self):
        records = csv.reader(self.cleaned_data["file"], delimiter=';')
         
        for line in records:
            if line[1] == "BLC_NAME":
                continue
            
            balance = Balance.objects.filter(name=line[1])
            if not balance.exists():
                balance = Balance()
                balance.name = line[1]
                balance.save()
            else:
                balance = balance.get()
               
               
            group = Group.objects.filter(name=line[3])
            if not group.exists():
                group = Group()
                group.name = line[3]
                group.save()
            else:
                group = group.get()
                
                
            budget_user_group = BudgetUserGroup.objects.filter(name=line[5],group=group.pk)
            if not budget_user_group.exists():
                budget_user_group = BudgetUserGroup()
                budget_user_group.group = group
                budget_user_group.name = line[5]
                budget_user_group.save()
            else:
                budget_user_group = budget_user_group.get()
                
                
            budget_user = BudgetUser.objects.filter(name=line[7],group=budget_user_group.pk)
            if not budget_user.exists():
                budget_user = BudgetUser()
                budget_user.group = budget_user_group
                budget_user.name = line[7]
                budget_user.save()
            else:
                budget_user = budget_user.get()
            
            
            political_branch = PoliticalBranch.objects.filter(name=line[9])
            if not political_branch.exists():
                political_branch = PoliticalBranch()
                political_branch.name = line[9]
                political_branch.save()
            else:
                political_branch = political_branch.get()
                
                
            programme = Programme.objects.filter(name=line[11])
            if not programme.exists():
                programme = Programme()
                programme.name = line[11]
                programme.save()
            else:
                programme = programme.get()
            
            
            category = Category.objects.filter(name=line[13], balance=balance.pk, budget_user=budget_user.pk, political_branch=political_branch.pk, programme=programme.pk)
            if not category.exists():
                category = Category()
                category.balance = balance
                category.budget_user = budget_user
                category.political_branch = political_branch
                category.programme = programme
                category.name = line[13]
                category.save()
            else:
                category = category.get()
            
            
            item = Item.objects.filter(category=category.pk, budget_year = self.cleaned_data["year"])
            if not item.exists():
                item = Item()
                item.category = category
                item.budget_year = self.cleaned_data["year"]
                item.value = float(line[14].replace(",","."))
                item.save()
            else:
                item = item.get()
                        