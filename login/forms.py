from django import forms

class ConnexionForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'5','autofocus': True, 'class':'input_area', }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class':'input_area', 'placeholder':'••••••••'}))