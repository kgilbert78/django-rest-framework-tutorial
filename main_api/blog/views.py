from collections.abc import Callable, Iterable, Mapping
import threading
from typing import Any

from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail

from .models import Post, PostRating
from .serializer import PostSerializer, PostRatingSerializer

class HandleNotifications(threading.Thread):
    def __init__(self, message, subject, recipient_list):
        self.message = message
        self.subject = subject
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        from_email = "kyle@kylegilbert.dev"
        send_mail(self.subject, self.message, from_email, self.recipient_list, fail_silently=False)

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts
    
    # need to override viewset's built in "create" so you can connect the post & rating
    def create(self, request, *args, **kwargs):
        data = request.data

        # create PostRating first so that...
        new_rating = PostRating.objects.create(likes=data["ratings"]["likes"], dislikes=data["ratings"]["dislikes"])
        new_rating.save()

        # ...you can assign it to the rating field when you create the Post
        new_post = Post.objects.create(title=data["title"], body=data["body"], ratings=new_rating)
        new_post.save()

        HandleNotifications("Blog post notification", f"There is a new post called {new_post.title}", ["kyle@kylegilbert.dev"]).start()

        serializer = PostSerializer(new_post)
        
        return Response(serializer.data)

# data structure for postman/frontend
# {
#     "title": "Test Post",
#     "body": "This is the text of my post.",
#     "ratings": {
#         "likes": 9,
#         "dislikes": 1
#     }
# }
    
class PostRatingViewSet(viewsets.ModelViewSet):
    serializer_class = PostRatingSerializer

    def get_queryset(self):
        ratings = PostRating.objects.all()
        return ratings
    
# NOTE:
# needs error handling for if it can't create the post but it already created the rating, so it doesn't leave a post-less rating in the PostRating table.