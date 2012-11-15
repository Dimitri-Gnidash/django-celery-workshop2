from django.views.generic import CreateView

from forms import NotifyScaledImageForm


class ScaleImageView(CreateView):
    template_name = "home.html"
    form_class = NotifyScaledImageForm

    success_url = "/"

    def post(self, *args, **kwargs):
        result = super(ScaleImageView, self).post(*args, **kwargs)
        return result

    def form_valid(self, form):
        super(ScaleImageView, self).form_valid(form)

        return self.render_to_response(self.get_context_data(form=form,
                                       success=True))
