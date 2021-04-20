from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #parameters = {'Name' : 'Mahima', 'Place' : 'South Korea'}
    return render(request, 'index.html')#, parameters)
    #return HttpResponse('Hello, This is Home Page!')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    wordcnt = request.POST.get('wordcnt', 'off')
    reverse = request.POST.get('reverse', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed=djtext.upper()
        # for char in djtext:
        #     analyzed = analyzed + char.upper()
        params = {'purpose':' Changed to UPPER CASE ', 'analyzed_text': analyzed}
        djtext = analyzed 
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != '\n' and char!='\r': #\r is added because newline remover was not working as we have added <pre> in analyze.html
                analyzed = analyzed + char
        params = {'purpose':' new line removed ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose':' new line removed ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if wordcnt == "on":
        cnt=0
        for x in djtext.split():
            cnt+=1
        params = {'purpose':' character counted ', 'analyzed_text': cnt}
        djtext = cnt
        # return render(request, 'analyze.html', params)

    if reverse == "on":
        analyzed = djtext[::-1]
        params = {'purpose':' reversed the string ', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc!='on' and fullcaps !='on' and newlineremover!='on' and extraspaceremover!='on' and wordcnt!='on' and reverse!='on'):
        return HttpResponse('!! E R R O R !!')

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse('Error')    
# def removePunc(request):
#     get_text = request.GET.get('text', 'default')
#     print(get_text) 
#     #print(request.GET.get('text', 'default'))
#     return HttpResponse('''Remove Puncuations <br>
#     <a href="/">Back</a>''')

# def capFirst(request):
#     return HttpResponse('''Captilize First <br>
#     <a href="/">Back</a>''')

# def newLineRemove(request):
#     return HttpResponse('''Remove New Line <br>
#     <a href="/">Back</a>''')

# def spaceRemove(request):
#     return HttpResponse('''Remove Spaces <br>
#     <a href="/">Back</a>''')

# def charCount(request):
#     return HttpResponse('''Count Character <br>
#     <a href="/">Back</a>''')

# def about (request):
#     return HttpResponse('Mahima Jain')

# #read a text file
# def readText(request):
#     with open('F:/Django Course/1st.txt', 'r') as f:
#         st = f.read()
#     return HttpResponse(st)

# #personal navigator
# def personalNavigator(request):
#     site = '''<h2>Navigation to different websites<br></h2>
#             <a href="https://www.youtube.com/"> Youtube </a><br> 
#             <a href="https://www.instagram.com/jn_mahima9/"> Instagram </a><br>
#             <a href="https://www.google.com/"> Google </a>'''
#     return HttpResponse(site)