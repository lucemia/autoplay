from .models import ScreenShot
from django.http import JsonResponse
from .tasks import tap, swipe
# Create your views here.


def screenshot_view(request):
    screen_shot = ScreenShot.objects.all().order_by('-created')[0]

    return JsonResponse({'url': screen_shot.file.url})


def tap_view(request):
    x = request.GET.get('x')
    y = request.GET.get('y')

    tap(x, y)
    return JsonResponse({})


def swipe_view(request):
    x1 = request.GET.get('x1')
    y1 = request.GET.get('y1')

    x2 = request.GET.get('x2')
    y2 = request.GET.get('y2')

    swipe(x1, y1, x2, y2)
    return JsonResponse({})
