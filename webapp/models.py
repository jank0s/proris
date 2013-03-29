from django.db import models

class Balance(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    balance = models.ForeignKey(Balance)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class BudgetUserGroup(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class BudgetUser(models.Model):
    group = models.ForeignKey(BudgetUserGroup)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class PoliticalBranch(models.Model):
    budget_user = models.ForeignKey(BudgetUser)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Programme(models.Model):
    political_branch = models.ForeignKey(PoliticalBranch)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    programme = models.ForeignKey(Programme)
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category)
    budget_year = models.IntegerField()
    value = models.FloatField()
    def __unicode__(self):
        return self.category + "(" + self.budget_year + ")" + self.value