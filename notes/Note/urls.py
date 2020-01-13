from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.note_list, name='note_list'),
    # path('', views.NotesList.as_view(), name='note_list'),
    path('note/new/', views.NoteCreate.as_view(), name='note_new'),
    path('note/view/<uuid:pk>', views.NoteDetailView.as_view(), name='note_details'),
    path('note/edit/<uuid:pk>', views.NoteUpdate.as_view(), name='note_edit'),
    path('note/delete/<uuid:pk>', views.NoteDelete.as_view(), name='note_delete'),
]