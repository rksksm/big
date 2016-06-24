from django.contrib import admin
from news.models import *
from tinymce.widgets import TinyMCE


class SectionAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title',]
	formfield_overrides = {
        HTMLField: {'widget': TinyMCE(attrs={'size':'200'})},
    }
class CardAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title',]
class BreakingAdmin(admin.ModelAdmin):
	search_fields = ['text']
	list_display = ['text',]
class SlideAdmin(admin.ModelAdmin):
	search_fields = ['text']
	list_display = ['text',]


admin.site.register(Section, SectionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Breaking, BreakingAdmin)
admin.site.register(Slide, SlideAdmin)