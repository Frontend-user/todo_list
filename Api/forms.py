from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(max_length=200)


class ListForm(forms.Form):
    name = forms.CharField(max_length=100)