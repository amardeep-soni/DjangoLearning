from django import forms


class DjangoForm(forms.Form):
    value1 = forms.CharField(
        label="value 1",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    value2 = forms.CharField(
        label="value 1",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
