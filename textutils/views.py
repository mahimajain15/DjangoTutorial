from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #parameters = {'Name' : 'Mahima', 'Place' : 'South Korea'}
    return render(request, 'index.html')#, parameters)
    #return HttpResponse('Hello, This is Home Page!')

def removePunc(request):
    get_text = request.GET.get('text', 'default')
    print(get_text) 
    #print(request.GET.get('text', 'default'))
    return HttpResponse('''Remove Puncuations <br>
    <a href="/">Back</a>''')

def capFirst(request):
    return HttpResponse('''Captilize First <br>
    <a href="/">Back</a>''')

def newLineRemove(request):
    return HttpResponse('''Remove New Line <br>
    <a href="/">Back</a>''')

def spaceRemove(request):
    return HttpResponse('''Remove Spaces <br>
    <a href="/">Back</a>''')

def charCount(request):
    return HttpResponse('''Count Character <br>
    <a href="/">Back</a>''')

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