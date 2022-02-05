from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select, DateInput, TimeInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'importance', 'date', 'time', 'email']

        widgets = {
            'title':  TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'task': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание'
                }),
            'importance': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Выберите срочность'
                }),
            'date': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
            'time': TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите email, если хотите получать уведемления'
                }),
        }
