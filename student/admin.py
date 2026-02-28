from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'class_name', 'phone_number', 'village', 'admission_date')
    search_fields = ('name', 'phone_number', 'village')
    list_filter = ('class_name', 'admission_date')