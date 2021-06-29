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