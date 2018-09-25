from django.http import HttpResponseRedirect


def decorator(func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('uname'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return wrapper

