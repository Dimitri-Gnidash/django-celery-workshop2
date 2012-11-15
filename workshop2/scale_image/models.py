import uuid
from django.db import models

from storages.backends.s3boto import S3BotoStorage


def unique_filename_with_section(section):
    """
    Create a unique filename with section name included
    """
    def _inner(instance, filename):
        unique_name = uuid.uuid4()

        return "%(section)s/%(uuid)s-%(filename)s" % {"section": section,
                                                     "uuid": unique_name,
                                                     "filename": filename}
    return _inner


class NotifyScaledImage(models.Model):
    image = models.FileField(storage=S3BotoStorage(), upload_to=unique_filename_with_section('workshop2'))
    notify = models.EmailField()
    name = models.CharField(max_length=255)
