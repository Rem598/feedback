from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.db.models import Q 


from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Thank you for your feedback."
            return render(request, 'home.html', {'form': FeedbackForm(), 'message': message})
    else:
        form = FeedbackForm()
    
    return render(request, 'home.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')


def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    
    return render(request, 'submit_feedback.html', {'form': form})


