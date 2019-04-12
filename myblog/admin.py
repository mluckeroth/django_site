from django.contrib import admin
from myblog.models import Post, Category


class CatergoryInline(admin.StackedInline):
    model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CatergoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)