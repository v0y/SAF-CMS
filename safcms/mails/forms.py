from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    subject = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': "Podaj poprawny adres email"})
    text = forms.CharField(widget=forms.Textarea, required=True)
