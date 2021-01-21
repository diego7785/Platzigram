## Post views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required # Hace que se requiera estar logueado para poder acceder a esta pagina
def list_posts(req):
    ## List of existing posts
    return render(req,'posts/feed.html', {
        'posts': posts
    })


@login_required
def create_post(req):
    if req.method == 'POST':
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else: 
        form = PostForm()
        return render(
            req, 
            template_name='posts/new.html',
            context={
                'form': form,
                'user': req.user,
                'profile': req.user.profile
            }
        )