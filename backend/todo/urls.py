from rest_framework.urls import path
from .views import TodoDeleteView, TodoListCreateView, TodoUpdateView

urlpatterns = [
    path("", TodoListCreateView.as_view(), name="create_fetch_tasks"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="delete_notes"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="update_notes")
]
