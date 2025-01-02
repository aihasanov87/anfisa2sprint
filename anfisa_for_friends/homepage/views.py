from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import Category, IceCream


def index(request):
    template_name = 'homepage/index.html'

    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    
    # Запрос:
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description').filter(
    #         Q(is_published=True)
    #         & Q(is_on_main=True)
    #         | Q(title__contains='пломбир')
    #         & Q(is_published=True)).order_by('title')[1:4]

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }

    return render(request, template_name, context)
