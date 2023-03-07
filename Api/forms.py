from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(max_length=200)