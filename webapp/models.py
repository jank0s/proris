from django.db import models

class Balance(models.Model):
    name = models.CharField(max_length=200)

class Group(models.Model):
    balance = models.ForeignKey(Balance)
    name = models.CharField(max_length=200)

class BudgetUserGroup(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=200)

class BudgetUser(models.Model):
    group = models.ForeignKey(BudgetUserGroup)
    name = models.CharField(max_length=200)

class PoliticalBranch(models.Model):
    budget_user = models.ForeignKey(BudgetUser)
    name = models.CharField(max_length=200)

class Programme(models.Model):
    political_branch = models.ForeignKey(PoliticalBranch)
    name = models.CharField(max_length=200)

class Category(models.Model):
    programme = models.ForeignKey(Programme)
    name = models.CharField(max_length=200)

class Item(models.Model):
    category = models.ForeignKey(Category)
    budget_year = models.IntegerField()
    value = models.FloatField()