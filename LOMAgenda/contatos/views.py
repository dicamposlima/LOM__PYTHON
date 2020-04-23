from django.shortcuts import render,\
    get_object_or_404,\
    redirect
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from .models import Contato


def index(request):
    contatos = Contato.objects\
        .order_by('-id')\
        .filter(show=True)
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def view(request, contato_id: int):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.show:
        raise Http404()
    return render(request, 'contatos/view.html', {
        'contato': contato
    })


def search(request):
    q = request.GET.get('q')
    if q is None or not q:
        messages.add_message(request,
                             messages.ERROR,
                             'Busca inválida.')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects\
        .annotate(nome_completo=campos)\
        .filter(Q(nome_completo__icontains=q) |
                Q(email__icontains=q) |
                Q(telefone__icontains=q),
                show=True)\
        .order_by('-id')
    # print(contatos.query)
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/search.html', {
        'contatos': contatos
    })


"""
def view(request, contato_id: int):
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/view.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()
"""