from django.shortcuts import render
from django.views.generic.edit import FormView
from things.forms import ThingForm

#def home(request):
#    return render(request, 'form.html', {'form': ThingForm})

class home(FormView):

    """Display the create task screen and handle creating tasks."""

    model = ThingForm
    form_class = ThingForm
    template_name = "home.html"

    def get_form_kwargs(self, **kwargs):
        """Pass the current user to the create task form."""

        kwargs = super().get_form_kwargs(**kwargs)
        return kwargs

    def form_valid(self, form):
        #self.object = form.save()
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return "/"
