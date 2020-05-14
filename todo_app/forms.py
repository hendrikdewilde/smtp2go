import logging
from datetime import datetime

from django import forms

from todo_app.models import TodoList

log = logging.getLogger(__name__)


class TodoAppAddForm(forms.ModelForm):

    class Meta:
        model = TodoList

        fields = ['title', 'description']

        exclude = []

    def __init__(self, *args, **kwargs):
        super(TodoAppAddForm, self).__init__(*args, **kwargs)


class TodoAppUpdateForm(forms.ModelForm):
    created_timestamp_display = forms.DateTimeField(required=False)

    class Meta:
        model = TodoList

        fields = ['title', 'description',
                  'completed_flag', 'completed_timestamp']

        exclude = []

    def __init__(self, *args, **kwargs):
        super(TodoAppUpdateForm, self).__init__(*args, **kwargs)
        self.initial['created_timestamp_display'] = self.instance.created_timestamp
        self.fields['created_timestamp_display'].widget.attrs['readonly'] = True
        self.fields['completed_timestamp'].widget.attrs['readonly'] = True


class TodoAppDeleteForm(forms.Form):
    confirm = forms.BooleanField(label='Are you sure you want to delete this '
                                       'record?', required=False)
