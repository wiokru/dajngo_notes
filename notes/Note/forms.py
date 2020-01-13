from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
        'created_date': forms.DateInput(attrs={'disabled': True}),
        'modified_date': forms.DateInput(attrs={'disabled': True}),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(NoteForm, self).__init__(*args, **kwargs)
    #     self.fields['created_date'].disabled = True
    #     self.fields['modified_date'].disabled = True