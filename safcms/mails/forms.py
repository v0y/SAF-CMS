from django import forms


EMAIL_INVALID_MSG = "Podaj poprawny adres email"


class ContactForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    subject = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': EMAIL_INVALID_MSG})
    text = forms.CharField(widget=forms.Textarea, required=True)


class PrintOrderForm(forms.Form):
    COLOR_CHOICES = (
        ('Cielisty #FFF4DB', 'Cielisty #FFF4DB'),
        ('Biały #FFFFFF', 'Biały #FFFFFF'),
        ('Niebieski #0063A1', 'Niebieski #0063A1'),
        ('Żółty #FFF200', 'Żółty #FFF200'),
        ('Czarny #000000', 'Czarny #000000'),
        ('Czerwony #ED1D24', 'Czerwony #ED1D24'),
        ('Pomarańczowy #F7941E', 'Pomarańczowy #F7941E'),
        ('Ciemnozielony #30583B', 'Ciemnozielony #30583B'),
        ('Szaroniebieski #8899A2', 'Szaroniebieski #8899A2')
    )
    FILLING_CHOICES = (
        ('Solid', 'Solid (pełne) – najtwardsze'),
        ('Sparse High Density', 'Sparse High Density (rzadki, wysokiej gęstości)'),
        ('Sparse Low Density',
            'Sparse Low Density (rzadki, niskiej gęstości) – wypełnienie '
            'przypominające plaster miodu')
    )
    RESOLUTION_CHOICES = (
        ('0.254 mm', '0.254 mm (0.010 cala)'),
        ('0.3302 mm', '0.3302 mm (0.013 cala)')
    )

    name = forms.CharField(max_length=128, required=False)
    phone = forms.CharField(max_length=128, required=False)
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': EMAIL_INVALID_MSG})
    file = forms.FileField(required=True)
    color = forms.ChoiceField(
        required=True, choices=COLOR_CHOICES)
    filling = forms.ChoiceField(required=True, choices=FILLING_CHOICES)
    resolution = forms.ChoiceField(required=True, choices=RESOLUTION_CHOICES)
