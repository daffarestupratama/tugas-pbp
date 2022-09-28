from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='judul', max_length=200)
    description = forms.CharField()