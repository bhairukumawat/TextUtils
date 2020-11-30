from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': "bhairu kumawat", 'place': "goloka thama"}
    return render(request, 'index.html', params)


def analyze(request):
    import string
    result = string.punctuation
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check checjbox values
    removepunc = request.POST.get('removepunc', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')



    fullcaps = request.POST.get('fullcaps', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed = ""
        for i in djtext:
            if i not in result:
                analyzed = analyzed + i
        params = {'purpose': 'RRemoved Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not( djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext=analyzed



    if(extraspaceremover != "on" and newlineremover!="on" and removepunc != "on" and removepunc != "on"):
        return HttpResponse("Error ")

    return render(request, 'analyze.html', params)

