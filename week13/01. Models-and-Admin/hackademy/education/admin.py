from django.contrib import admin

from education.models import Course


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'get_duration')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.duration.days // 30} months'

        return 'N/A'

    get_duration.short_description = 'Duration'
