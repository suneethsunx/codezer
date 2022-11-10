from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *


def index(request):
    codes = None
    query = None
    try:
        codes = CodeFile.objects.filter(user = request.user).order_by('-id')

        try:
            query = request.GET.get('query')
            codes = CodeFile.objects.filter(user = request.user, title__icontains = query).order_by('-id')
        except:
            pass

    except Exception as e:
        codes = []
    context = {
        'codes': codes,
        'query': query,
    }
    return render(request, 'base/index.html', context)


def get_code(request, pk):

    try:
        user = request.user
        code = CodeFile.objects.get(user = user, id = pk)

        context = {
            'code': code,
        }
    except:
        pass

    return render(request, 'base/get_code.html', context)


def get_other_code(request, link_id):

    try:
        code = CodeFile.objects.get(link_id = link_id, private = False)
        context = {
            'code': code,
        }
        return render(request, 'base/get_other_code.html', context)

    except:
        code = CodeFile.objects.get(link_id = link_id)
        context = {
            'code': code,
        }
        return render(request, 'base/get_other_code_error.html', context)

def search_code(request):
    
    try:
        global_query = request.GET.get('query')
        if global_query == '':
            return redirect('index')
        codes = CodeFile.objects.filter(private = False, title__icontains = global_query)
        context = {
            'codes': codes,
            'global_query': global_query,
        }
        return render(request, 'base/search_code.html', context)

    except:
        pass