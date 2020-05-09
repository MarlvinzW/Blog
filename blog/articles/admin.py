from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',  'date', 'time', )
    fieldsets = (
        ('Owner', {'fields': ('user',)}),
        ('Title', {'fields': ('title',)}),
        ('Body', {'fields': ('body', )}),
    )


admin.site.register(Articles, ArticlesAdmin)
