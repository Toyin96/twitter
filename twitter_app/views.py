from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweet


# Create your views here.
def home(request):
    tweets = Tweet.objects.all()

    context = {"tweets": tweets}
    return render(request, 'twitter_app/homepage.html', context)


def create_tweet(request):
    if request.method != "POST":
        form = TweetForm()
    else:
        form = TweetForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("twitter_app:home")

    context = {"form": form}
    return render(request, "twitter_app/new_tweet.html", context)
