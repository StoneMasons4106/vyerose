from django.contrib import admin
from .models import TextField

# Register your models here.

class TextFieldAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'about_title',
        'about_blurb'
    )

    ordering = (
        'name',
    )


admin.site.register(TextField, TextFieldAdmin)