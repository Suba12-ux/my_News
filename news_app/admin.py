from django.contrib import admin
from .models import Post

class visible(admin.ModelAdmin):
	list_display = ('id', 'title', 'watched', 'is_published', 'created_at', 'updated_at', )
	list_display_links = ('title',)
	list_editable = ('is_published',)
	readonly_fields = ('watched',)


admin.site.register(Post, visible)

