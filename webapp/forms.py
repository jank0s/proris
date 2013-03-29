from django import forms
import csv

class DataInput(forms.Form):
    file = forms.FileField()
    #place = forms.ModelChoiceField(queryset=Place.objects.all())
    
    def save(self):
        records = csv.reader(self.cleaned_data["file"])