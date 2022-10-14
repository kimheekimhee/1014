from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'reviews/index.html', context)
    
@login_required
def create(request):
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            return redirect('reviews:index')
    else:
        review = ReviewForm()
    context = {
        'review' : review,
    }
    return render(request, 'reviews/create.html', context)
