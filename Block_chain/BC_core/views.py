from django.shortcuts import render
from django.http import HttpResponse
from .models import Block
from django.template import loader


def index(request):
    """
    Главная вьюха
    """
    block_queryset = Block.objects.all().order_by('-id')[:50]   
    template = loader.get_template('BC_core/index.html')
    context = {
        'blocks': block_queryset
    }
    return HttpResponse(template.render(context))

def detail_block(request, block_id):
    """
    Вьюха детального представления
    """
    block = Block.objects.get(id=block_id)
    response = 'Height:{}|Hash block:{}|Time:{}\n'.format(block.id,\
        block.hash_block, block.time) 
    return HttpResponse(response)
