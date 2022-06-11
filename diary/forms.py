from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'title', 'content')

        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 50})
        }