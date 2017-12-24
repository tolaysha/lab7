from django.contrib import admin
from tutoring.models import *

# Register your models here.


class TutorsAdmin(admin.ModelAdmin):
    fields = (('name', 'surname', 'patronymic'), 'email', 'tel', 'birth_date', 'date_tutoring_begin', 'address',
              'region', 'edu', 'subjects')
    list_filter = ('region', ('edu', admin.RelatedOnlyFieldListFilter), ('subjects', admin.RelatedOnlyFieldListFilter),)
    list_display = ('surname', 'name', 'patronymic', 'email', 'tel', 'birth_date', 'date_tutoring_begin', 'address',
                    'region', 'get_edu', 'get_subjects')
    search_fields = ('name', 'surname', 'patronymic')
    list_per_page = 10


class SubjectsAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Education)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Regions)
admin.site.register(Tutors, TutorsAdmin)

admin.site.site_url = '/main/'
admin.site.site_header = 'Django Администрирование'
admin.site.index_title = 'Администрирование'
