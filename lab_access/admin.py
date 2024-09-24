from django.contrib import admin

from .models import User, AccessLog

# admin.site.register(User)
# admin.site.register(AccessLog)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'user_type', 'status', 'created_at')
    search_fields = ('name','student_id','user_type')
    list_filter = ('user_type', 'status', 'created_at')

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'time_stamp')
    search_fields = ('user__name', 'user__student-id')
    list_filter = ('action', 'timestamp')