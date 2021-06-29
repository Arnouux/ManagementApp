from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50','placeholder':'Catégorie'}))
    
class RenameForm(forms.Form):
    new_name = forms.CharField(label='',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50','placeholder':'Catégorie'}))
    
class DeleteForm(forms.Form):
    new_name = forms.CharField(label='',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50','placeholder':'Catégorie'}))
    
class NewUserForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'5'}))
    first_name = forms.CharField(label='Prénom',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50'}))
    last_name = forms.CharField(label='Nom',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50'}))
    mail = forms.CharField(label='mail',widget=forms.TextInput(
        attrs={'autocomplete':'off','maxlength':'50'}))