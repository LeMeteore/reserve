from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'index.html')

def results(request):
    return render_to_response('results.html')