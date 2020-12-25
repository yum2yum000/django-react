from django.shortcuts import render


def handler404(request, *args, **kwargs):
    return render(request, '404_test.html', {})


def handler500(request):
    return render(request, '500_test.html', {})
