from django.db import models

class Balance(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "        Balances"

class Group(models.Model):
    balance = models.ForeignKey(Balance)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "       Groups"

class BudgetUserGroup(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name 
    class Meta:
        verbose_name_plural = "      Budget User Groups"

class BudgetUser(models.Model):
    group = models.ForeignKey(BudgetUserGroup)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name    
    class Meta:
        verbose_name_plural = "     Budget Users"

class PoliticalBranch(models.Model):
    budget_user = models.ForeignKey(BudgetUser)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name  
    class Meta:
        verbose_name_plural = "    Political Branches"

class Programme(models.Model):
    political_branch = models.ForeignKey(PoliticalBranch)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name 
    class Meta:
        verbose_name_plural = "   Programmes"

class Category(models.Model):
    programme = models.ForeignKey(Programme)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = " Categories"

class Item(models.Model):
    category = models.ForeignKey(Category)
    budget_year = models.IntegerField()
    value = models.FloatField()
    def __unicode__(self):
        return self.category + "(" + self.budget_year + ")" + self.value
    class Meta:
        verbose_name_plural = "Items"
