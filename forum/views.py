from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required


def forum_index(request):
    categories = Category.objects.all()
    latest_posts = Post.objects.all().order_by('-date_posted')[:5]
    return render(request, 'forum/forum_index.html', {'categories': categories, 'latest_posts': latest_posts})


def forum_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category.id).order_by('-date_posted')
    return render(request, 'forum/forum_category.html', {'category': category, 'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    replies = Reply.objects.filter(post=post).order_by('-date_posted')
    return render(request, 'forum/post_detail.html', {'post': post, 'replies': replies})


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


@login_required()
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/edit_post.html', {'form': form})


@login_required()
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('forum_index')
    return render(request, 'forum/delete_post.html', {'post': post})


@login_required
def add_reply(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.post = post
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReplyForm()
    return render(request, 'forum/add_reply.html', {'form': form, 'post': post})


@login_required()
def update_reply(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save()
            return redirect('post_detail', post_id=reply.post.id)
    else:
        form = ReplyForm(instance=reply)
    return render(request, 'forum/edit_reply.html', {'form': form, 'post': reply.post})


@login_required()
def delete_reply(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    if request.method == 'POST':
        reply.delete()
        return redirect('forum_index')
    return render(request, 'forum/delete_reply.html', {"post": reply})


def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')
    else:
        results = None
    return render(request, 'forum/search.html', {'results': results, 'query': query})
