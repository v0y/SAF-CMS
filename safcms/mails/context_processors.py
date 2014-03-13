from .forms import ContactForm


def contact_form(request):
    form = ContactForm(request.POST or None)
    if request.POST and form.is_valid:
        print('send mail')

    return {'contact_form': form}

