from django.db import models


# Create your models here.
class TodoList(models.Model):
    created_timestamp = models.DateTimeField('Created timestamp',
                                             db_column='created_timestamp',
                                             auto_now_add=True)
    title = models.CharField('Title', db_column='title', max_length=50)
    description = models.TextField('Description', db_column='description',
                                   blank=True, null=True)
    completed_flag = models.BooleanField('Completed', blank=True,
                                         default=False)
    completed_timestamp = models.DateTimeField('Completed timestamp',
                                               db_column='completed_timestamp',
                                               blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
