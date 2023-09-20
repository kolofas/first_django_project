from django.shortcuts import render, redirect
import json
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
# from .words_list import context
from django.core.files.storage import FileSystemStorage
from . import FileDoer

# Create your views here.


# class HomeView(View):
# def get(self, request):
# if request.method == 'GET':
#  return HttpResponse('hello world')


def hello_page(request):
    return render(request, 'home.html')


def page_words_table(request):
    file = open('/home/keyenae/PycharmProjects/pythonProject1/my_first_proj/words_json', "r").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split(':')
        words1.append(word1)
        words2.append(word2)
    words_dict = dict(zip(words1, words2))
    context_dict = {'words_dict': words_dict}
    print(words_dict)
    print(context_dict)
    return render(request, 'words_list.html', context_dict)


def postuser(request):
    if request.method == 'GET':
        return render(request, 'add_words.html')
    else:
        print(request.POST['word1'])
        print(request.POST['word2'])
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        print(type(word1))
        with open('/home/keyenae/PycharmProjects/pythonProject1/my_first_proj/words_json', "a") as file:
            file.write(word1 + ':' + word2 + '\n')
        return redirect(hello_page)






