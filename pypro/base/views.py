from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<html>'
                        '<head><meta charset="utf-8"></head>'
                        '<body><h1>Olá Django!!</h1></body></html>',
                        content_type='text/html')
