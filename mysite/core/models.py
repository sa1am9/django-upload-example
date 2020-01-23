from django.db import models
import os

class Report(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    data = models.FileField(upload_to='data/')
    report = models.FileField(upload_to='reports/')

    def __str__(self):
        return f'{self.category}-{self.name}'

    def delete(self, *args, **kwargs):
        self.data.delete()
        self.report.delete()
        super().delete(*args, **kwargs)

    def filename(self):
        return os.path.basename(self.report.name)