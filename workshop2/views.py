from django.views.generic import FormView

from forms import ScaleImageForm


class ScaleImageView(FormView):
    template_name = "home.html"
    form_class = ScaleImageForm

    def post(self, *args, **kwargs):
        result = super(ScaleImageView, self).post(*args, **kwargs)
        return result

    def form_valid(self, form):
        #trigger scaling task
        #once the scaling task is done trigger email task
        return super(ScaleImageView, self).form_valid(form)
