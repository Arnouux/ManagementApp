from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'5','autofocus': True}))