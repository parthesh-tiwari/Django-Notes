from django.urls import path
from .views import CreateNotesView, DeleteNotesView, UpdateNotesView

urlpatterns = [
    path("notes/", CreateNotesView.as_view(), name='get_notes'),
    path("notes/delete/<int:pk>/", DeleteNotesView.as_view(), name='delete_notes'),
    path("notes/update/<int:pk>", UpdateNotesView.as_view(), name="update_notes")
]

