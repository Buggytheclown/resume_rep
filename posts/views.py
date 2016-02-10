from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .form import PostModel, ContactForm, ProfileForm, CommentModelForm
from posts.models import Post, ProfileModel, CommentModel


def view_profile(request, user_id):
    user_name = get_object_or_404 (User, id=user_id )
    user_profile = get_object_or_404(ProfileModel, user=user_name)
    user_post = Post.objects.all().filter(user=user_id)
    context = {
        'user_profile': user_profile,
        'user_post':user_post,
    }
    return render(request, 'posts/view_profile.html', context)

def profile(request):
    try:
        profile = request.user.profilemodel
    except ProfileModel.DoesNotExist:
        profile = ProfileModel(user=request.user)

    if request.method == 'POST':
        form_profile = ProfileForm(request.POST, request.FILES, instance=profile)
        if form_profile.is_valid():
            form_profile.save()
            return redirect('home')
    else:
        form_profile = ProfileForm(instance=profile)

    user_post = Post.objects.all().filter(user=request.user)
    context = {
        'user_post':user_post,
        'form_profile': form_profile,
    }
    return render(request, 'posts/profile.html', context)


def about(request):
    return render(request, 'posts/about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    form_title = 'Contact form:'
    if request.method == 'POST' and form.is_valid():
        form_title = 'Your message was sent successfully!'
        form.save()
        form = ''
    context = {
        'form_title': form_title,
        'form': form,
    }
    return render(request, 'posts/contact.html', context)


def posts_list(request):
    model_title = Post.objects.all()
    query = request.GET.get('q')
    if query:
        model_title = Post.objects.all().filter(title__icontains=query)
    paginator = Paginator(model_title, 5)
    page = request.GET.get('page')
    try:
        model_title_p = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        model_title_p = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        model_title_p = paginator.page(paginator.num_pages)
    context = {
        'model_title': model_title_p
    }
    return render(request, 'posts/home.html', context)


def posts_create(request):
    if not request.user.is_authenticated() and not request.user.is_superuser:
        raise Http404
    form = PostModel(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Post successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    comments = CommentModel.objects.filter(in_post=id).order_by('-timestamp')
    form = CommentModelForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pre_form = form.save(commit=False)
        pre_form.user = request.user
        pre_form.in_post_id = id
        pre_form.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        'instance': instance,
        'comments':comments,
        'form':form,
    }
    return render(request, 'posts/detail.html', context)


def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    author = request.user == instance.user

    if not author and not request.user.is_superuser:
        raise Http404()

    form = PostModel(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        # some stuff there
        instance.save()
        messages.success(request, 'Post successfully edited')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    author = request.user == instance.user

    if not author and not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post: %s - was successfully deleted" % (instance.title))
    return redirect('home')
