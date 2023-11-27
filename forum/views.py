from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment, Reply, Like, Dislike, CommentLike, CommentDislike
from .forms import PostForm, CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def forum_index(requests):
    categories = Category.objects.all()
    latest_posts = Post.objects.all().order_by('-date_posted')[:5] # Get the 5 latest posts
    return render(requests, 'forum/forum_index.html', {'categories': categories, 'latest_posts': latest_posts})

def forum_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category.id).order_by('-date_posted')
    return render(request, 'forum/forum_category.html', {'category': category, 'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/post_detail.html', {'post': post})

def forum_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    posts = Post.objects.filter(title__contains=search_text)
    return render(request, 'forum/forum_search.html', {'posts': posts})

# Create a new post
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the post to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'forum/post_detail.html', {'post': post})
    else:
        form = PostForm()
    return render(request, 'forum/add_post.html', {'form': form})

# Add a comment to a post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment to the database
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return render(request, 'forum/post_detail.html', {'post': post})
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment.html', {'form': form})

# Add a reply to a comment
@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            # Save the reply to the database
            reply = form.save(commit=False)
            reply.author = request.user
            reply.comment = comment
            reply.save()
            return render(request, 'forum/post_detail.html', {'post': comment.post})
    else:
        form = ReplyForm()
    return render(request, 'forum/add_reply.html', {'form': form})