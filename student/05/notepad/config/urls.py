from django.urls import path
from note.views import NoteDetailView, NoteListView

urlpatterns = [
    path('', NoteListView.as_view()),
    path('<int:pk>', NoteDetailView.as_view()),
]