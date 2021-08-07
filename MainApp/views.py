from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.contrib.auth import models
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    fname = 'Георгий'
    lname = 'Репченков'
    mname = 'Олегович'
    tel = '8-800-555-35-35'
    email = 'email@yandex.ru'
    return HttpResponse(f'Имя: <b>{fname}</b><br>'
                        f'Отчество: <b>{lname}</b><br>'
                        f'Фамилия: <b>{mname}</b><br>'
                        f'Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')

def items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)

def item_details(request, id):
    try:
        item = Item.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": item
    }
    return render(request, "item_page.html", context)
