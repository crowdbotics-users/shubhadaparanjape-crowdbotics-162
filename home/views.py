from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'spirit', 'url': 'http://pypi.python.org/pypi/spirit/1.7.0'},
	{'name':'Misago', 'url': 'http://pypi.python.org/pypi/Misago/0.14.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
