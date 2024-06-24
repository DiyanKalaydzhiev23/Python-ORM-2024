from django.contrib import admin
from main_app.models import EventRegistration, Student, Supplier, Course, Movie


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'participant_name', 'registration_date')
    list_filter = ('event_name', 'registration_date')
    search_fields = ('event_name', 'participant_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'genre')
    list_filter = ('release_year', 'genre')
    search_fields = ('title', 'director')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "grade")
    list_filter = ("age", "grade", "date_of_birth")
    search_fields = ("first_name", )

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'date_of_birth'),
            # 'classes': ('collapse', ) - bonus
        }),
        ('Academic Information', {
            'fields': ('grade', ),
        })
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name', 'phone')
    search_fields = ('email', 'contact_person', 'phone')
    list_per_page = 20

    fieldsets = (
        ('Information', {
            'fields': ('name', 'contact_person', 'email', 'address'),
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'lecturer', 'price', 'start_date')
    list_filter = ('is_published', 'lecturer')
    search_fields = ('lecturer', 'title')
    readonly_fields = ('start_date', )

    fieldsets = (
        ('Course Information', {
            'fields': ('title', 'lecturer', 'price', 'start_date', 'is_published'),
        }),
        ('Description', {
            'fields': ('description', ),
        })
    )






