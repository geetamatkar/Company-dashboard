from django.http import HttpResponse, JsonResponse

def home_page(request):
    print('Home page requested')
    friends=[
        'Sakshi',
        'Shalaka'
    ]
    return JsonResponse(friends, safe=False)