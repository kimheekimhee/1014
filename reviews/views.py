from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        review = ReviewForm(request.POST)
        if review.is_valid():
            review.save()
            return redirect("reviews:index")
    else:
        review = ReviewForm()
    context = {
        "review": review,
    }
    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/update.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")
