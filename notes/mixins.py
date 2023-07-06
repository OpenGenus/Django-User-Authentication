from django.core.exceptions import PermissionDenied
from django.views.generic.edit import SingleObjectMixin


class NoteOwnerRequiredMixin(SingleObjectMixin):
    def get_object(self, queryset=None):
        note = super().get_object(queryset)
        if not note.is_owner(self.request.user):
            raise PermissionDenied
        return note
