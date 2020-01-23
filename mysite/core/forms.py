from django import forms

from .models import Report

choices = [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('category', 'name', 'data')


