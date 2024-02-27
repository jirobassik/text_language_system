from django.http import HttpResponse


def main_view(request):
    text = '12345'
    return HttpResponse(text, content_type='text/plain')
