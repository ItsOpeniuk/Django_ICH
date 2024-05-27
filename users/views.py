from django.http import HttpResponse, HttpRequest

def greet(request: HttpRequest, user_name) -> HttpResponse:
    resp = f'<h1>Hello, {user_name}! all is work!!</h1>'
    return HttpResponse(resp)
