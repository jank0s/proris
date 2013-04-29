from django.db import models


class Balance(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "        Balances"


class Group(models.Model):
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
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "    Political Branches"


class Programme(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "   Programmes"


class Category(models.Model):
    balance = models.ForeignKey(Balance)
    budget_user = models.ForeignKey(BudgetUser)
    political_branch = models.ForeignKey(PoliticalBranch)
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
        return self.category.name + " (" + self.budget_year.__str__() + ") "

    class Meta:
        verbose_name_plural = "Items"
