from django.db import models

# Create your models here.


class Education(models.Model):
    id_university = models.AutoField(primary_key=True)
    name_university = models.CharField(max_length=100, verbose_name='Университет')

    def __str__(self):
        return self.name_university

    class Meta:
        verbose_name_plural = "Университеты"
        verbose_name = "Университет"


class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True)
    name_subject = models.CharField(max_length=100, verbose_name='Предмет')

    def __str__(self):
        return self.name_subject

    class Meta:
        verbose_name_plural = "Предметы"
        verbose_name = "Предмет"


class Regions(models.Model):
    id_region = models.AutoField(primary_key=True)
    name_region = models.CharField(max_length=100, verbose_name='Регион')

    def __str__(self):
        return self.name_region

    class Meta:
        verbose_name_plural = "Регионы"
        verbose_name = "Регион"


class Tutors(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, verbose_name='Имя')
    surname = models.CharField(max_length=45, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=45, verbose_name='Отчество')
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    tel = models.CharField(max_length=20, verbose_name='Номер телефона')
    birth_date = models.DateField(verbose_name='Дата рождения')
    date_tutoring_begin = models.DateField(verbose_name='Дата начала преподавания')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, verbose_name='Регион')
    edu = models.ManyToManyField(Education, verbose_name='Образование')
    subjects = models.ManyToManyField(Subjects, verbose_name='Преподаваемые предметы')

    def __str__(self):
        return '%s %s %s' % (self.name, self.surname, self.patronymic)

    def get_edu(self):
        return "\n".join([e.name_university for e in self.edu.all()])
    get_edu.short_description = 'Образование'

    def get_subjects(self):
        return ", ".join([s.name_subject for s in self.subjects.all()])
    get_subjects.short_description = 'Преподаваемые предметы'

    class Meta:
        verbose_name_plural = "Репетиторы"
        verbose_name = "Репетитор"
