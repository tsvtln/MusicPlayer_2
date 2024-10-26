from django import forms

from MusicPlayer_2.mixins import PlaceholderMixin
from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    pass
