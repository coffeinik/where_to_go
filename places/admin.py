from django.contrib import admin
from django.utils.html import mark_safe
from .models import Place, PlaceImage



class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ["image_preview"]
    fields = ('image', 'image_preview', 'order_number')
    def image_preview(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url = obj.image.url, 
            height=200,
        )
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):    
    inlines = [
        PlaceImageInline,
    ]