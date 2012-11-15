import json
from django.views.generic import CreateView
from stallion.images import tasks as image_tasks
from stallion.email import tasks as email_tasks
from celery.task import group, chord
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
        subtasks = [image_tasks.scale_image.si(self.object.image.name, 50),
            image_tasks.scale_image.si(self.object.image.name, 100),
            image_tasks.scale_image.si(self.object.image.name, 150),
            image_tasks.scale_image.si(self.object.image.name, 200),
            image_tasks.scale_image.si(self.object.image.name, 250),
            image_tasks.scale_image.si(self.object.image.name, 300),
            image_tasks.scale_image.si(self.object.image.name, 400)]

        subtasks_async = group(subtasks).apply_async()

        upon_completion = email_tasks.send_email.si("dimitri@bnotions.com",
                                                    [self.object.notify],
                                                    "Yo",
                                                    "All your images are scaled")

        chord(subtasks)(upon_completion)

        task_ids = [t.task_id for t in subtasks_async.subtasks]

        return self.render_to_response(self.get_context_data(form=form,
                                       task_ids=json.dumps(task_ids),
                                       success=True))
