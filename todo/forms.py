from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=45,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter todo Item','aria-label':'Todo','aria-describedby':'add-btn'}
    ))