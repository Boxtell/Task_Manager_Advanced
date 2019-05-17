from django import forms
from .models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


def __init__(self):
    self.priority = 3


class SearchForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    task_name = forms.CharField(max_length=200,
                                required=False)
    task_status = forms.NullBooleanField()
    task_scope = forms.BooleanField(initial=True,
                                    required=False)

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date and end_date:
            if start_date > end_date or end_date < start_date:
                raise forms.ValidationError('Start date as to be lower than end date')
