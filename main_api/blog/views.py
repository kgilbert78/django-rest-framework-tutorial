from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post, PostRating
from .serializer import PostSerializer, PostRatingSerializer


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