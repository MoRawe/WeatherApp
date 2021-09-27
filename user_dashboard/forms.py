from django import forms


class SingleFileForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    csv = forms.FileField()
