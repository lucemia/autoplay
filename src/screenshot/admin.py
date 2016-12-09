from django.contrib import admin
from .models import ScreenShot
from django.utils.html import format_html

# Register your models here.


class ScreenShotAdmin(admin.ModelAdmin):
    list_display = ('created', 'preview')

    def preview(self, obj):
        return format_html(
            u'<a href="{}"><img style="max-height:200px" src="{}"></a>',
            obj.file.url, obj.file.url
        )


admin.site.register(ScreenShot, ScreenShotAdmin)
