from django.shortcuts import render
from django.http import HttpResponse
from .models import Block
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    """
    Главная вьюха
    """
    block_queryset = Block.objects.all().order_by('-id')
    paginator = Paginator(block_queryset, 4)
    title = 'Главная страница'
    
    page = request.GET.get('page')
    try:
        blocks = paginator.page(page)
    except PageNotAnInteger:        
        # Если страница не является целым числом, поставим первую страницу 
        blocks = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов 
        blocks = paginator.page(paginator.num_pages)
    context = {
        'blocks': blocks,
        'page': page,
        'title': title,
    }
    return render(request, "BC_core/index.html", context)


def detail_block(request, block_id):
    """
    Вьюха детального представления
    """
    blocks = Block.objects.get(id=block_id)
    title = 'Детальное представление блока {}'.format(block_id)
    context = {
        'blocks': blocks,
        'title': title,
    }
    return render(request, "BC_core/detail_block.html", context)
