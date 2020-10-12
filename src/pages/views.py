from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_result = {
        'my_text': 'Testing',
        'my_number': 123456,
        'my_list': [123, 3223, 23123]
    }
    return render(request, 'home.html', my_result)
