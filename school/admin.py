from django.contrib import admin
from .models import Category, Scholar, Book, Lesson, Branch, AboutPage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Scholar)
class ScholarAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch')
    search_fields = ('name', 'bio')
    list_filter = ('branch',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'author')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'scholar', 'branch')
    list_filter = ('scholar', 'branch')
    search_fields = ('title',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('country', 'city')
    search_fields = ('country', 'city', 'address')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('المحتوى الأساسي', {
            'fields': ('title', 'message', 'objectives')
        }),
        ('الشعار', {
            'fields': ('logo',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # السماح بالإضافة فقط إذا لم يكن هناك سجل
        return not AboutPage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # منع الحذف
        return False
