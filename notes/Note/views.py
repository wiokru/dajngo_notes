from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import NoteForm
from .models import Note
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def note_list(request):
    all_notes = Note.objects.all().order_by('created_date').reverse()
    return render(request, 'note_list.html', {'notes': all_notes})

# def note_new(request):
#     if request.method == "POST":
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             # note.author = request.user
#             note.published_date = timezone.now()
#             note.modified_date = timezone.now()
#             note.save()
#             return redirect('note_list')
#     else:
#         form = NoteForm()
#     return render(request, 'note_new.html', {'form': form})


class NotesList (generic.ListView):
    model = Note
    template_name = 'note_list.html'

# READ
class NoteDetailView (generic.DetailView):
    model = Note
    template_name = 'note_details.html'


# CREATE
class NoteCreate (generic.edit.CreateView):
    model = Note
    fields = '__all__'
    template_name = 'note_new.html'
    success_url = reverse_lazy('note_list')

    def get_initial(self):
        date = timezone.now()
        return {
            'published_date': date,
            'modified_date': date,
        }

# UPDATE
class NoteUpdate (generic.edit.UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'note_edit.html'
    success_url = reverse_lazy('note_list')

    def get_initial(self):
        date = timezone.now()
        return {
            'modified_date': date,
        }

# DELETE
class NoteDelete (generic.edit.DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('note_list')

