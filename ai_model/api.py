from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.filter(is_published=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
