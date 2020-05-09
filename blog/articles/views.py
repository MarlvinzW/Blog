from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView

from blog import settings
from .forms import SearchForm
from .models import Articles

user = get_user_model()

""" Home Page"""


class Home(ListView):
    paginate_by = 10
    model = Articles
    template_name = 'articles/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = f'{settings.PLATFORM_NAME} | Home'
        context['form'] = SearchForm()
        return context


"""Search View"""


class Search(ListView):
    paginate_by = 6
    model = Articles
    template_name = 'articles/search.html'

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        if search:
            context['title'] = f'{settings.PLATFORM_NAME} | Search?={search}'
        else:
            context['title'] = f'{settings.PLATFORM_NAME} | Search'
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


""" View Article """


def view_article(request, article_id):
    context = {
        'title': f'{settings.PLATFORM_NAME} | Home',
        'articles': Articles.objects.filter(id=int(article_id))
    }
    return render(request, 'articles/view_article.html', context=context)
