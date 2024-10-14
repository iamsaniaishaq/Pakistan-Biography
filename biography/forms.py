from django import forms
from .models import PrimeMinisters

class PrimeMinisterForm(forms.ModelForm):
    class Meta:
        model = PrimeMinisters
        fields = [
            'name', 
            'english_bio', 
            'urdu_bio', 
            'english_achievements', 
            'urdu_achievements', 
            'youtube_link', 
            'background_color', 
            'term', 
            'image'  # Image field for file upload
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prime Minister Name'}),
            'english_bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'English Biography'}),
            'urdu_bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Urdu Biography'}),
            'english_achievements': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'English Achievements'}),
            'urdu_achievements': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Urdu Achievements'}),
            'youtube_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'YouTube Video Link'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Background Color (Hex Code)'}),
            'term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Term of Office'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})  # For file uploads (image)
        }
