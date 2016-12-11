from django.contrib import admin
from .models import ScreenShot, OrbMatcher, ImageHash
from django.utils.html import format_html

# Register your models here.


class ScreenShotAdmin(admin.ModelAdmin):
    list_display = ('created', 'preview')

    def preview(self, obj):
        return format_html(
            u'<a href="{}"><img style="max-height:200px" src="{}"></a>',
            obj.file.url, obj.file.url
        )


class OrbMatcherAdmin(admin.ModelAdmin):
    list_display = ('screenshot', 'preview', 'status', 'confidence')

    list_filter = ('status', )

    def preview(self, obj):
        return format_html(
            u'<a href="{}"><img style="max-height:200px" src="{}"></a>',
            obj.screenshot.file.url, obj.screenshot.file.url
        )


class ImageHashAdmin(admin.ModelAdmin):
    list_display = ('screenshot', 'ahash', 'phash', 'dhash', 'whash', 'preview')

    def preview(self, obj):
        return format_html(
            u'<a href="{}"><img style="max-height:200px" src="{}"></a>',
            obj.screenshot.file.url, obj.screenshot.file.url
        )

admin.site.register(ScreenShot, ScreenShotAdmin)
admin.site.register(OrbMatcher, OrbMatcherAdmin)
admin.site.register(ImageHash, ImageHashAdmin)
