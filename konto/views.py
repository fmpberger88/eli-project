from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forum.models import Post, Reply

# Create your views here.
def konto(request):
    user_post = Post.objects.filter(author=request.user)
    user_replies = Reply.objects.filter(author=request.user)
    return render(request, 'konto/account.html', {'user_post': user_post, 'user_replies': user_replies})
