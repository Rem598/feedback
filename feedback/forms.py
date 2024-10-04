from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your feedback'}),
            
        }
