from django.conf.urls import url
from .views import screenshot_view, tap_view, swipe_view
from django.views.generic import TemplateView


urlpatterns = [
    url(r'screen$', TemplateView.as_view(template_name="screen.html")),
    url(r'screenshot/', screenshot_view),
    url(r'tap/', tap_view),
    url(r'swipe/', swipe_view)
]
