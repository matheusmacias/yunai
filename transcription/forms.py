from .models import Transcription
from django import forms


class TranscriptionForm(forms.ModelForm):
    class Meta:
        model = Transcription
        fields = ["original_filename", "language", "file_size", "duration"]
        widgets = {
            "original_filename": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Nome do arquivo",
                }
            ),
            "language": forms.Select(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            ),
            "file_size": forms.NumberInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Tamanho em bytes",
                }
            ),
            "duration": forms.TimeInput(
                attrs={
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "HH:MM:SS",
                }
            ),
        }