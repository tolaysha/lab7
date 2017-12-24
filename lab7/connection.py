import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost', charset='utf8'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None
        self.charset = charset

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset=self.charset
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Education:
    def __init__(self, db_connection, name_university):
        self.db_connection = db_connection.connection
        self.name_university = name_university

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO образование (ВУЗ) VALUES (%s);", (self.name_university,))
        self.db_connection.commit()
        c.close()


class Subjects:
    def __init__(self, db_connection, name_subject):
        self.db_connection = db_connection.connection
        self.name_subject = name_subject

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO предметы (Название_предмета) VALUES (%s);", (self.name_subject,))
        self.db_connection.commit()
        c.close()


class Regions:
    def __init__(self, db_connection, name_region):
        self.db_connection = db_connection.connection
        self.name_region = name_region

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO `tutoring`.`регионы` (`Регион`) VALUES (%s);", (self.name_region,))
        self.db_connection.commit()
        c.close()


class Tutors:
    def __init__(self, db_connection, name, surname, patronymic, email, tel, birth_date, date_tutoring_begin, address, id_region):
        self.db_connection = db_connection.connection
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.email = email
        self.tel = tel
        self.birth_date = birth_date
        self.date_tutoring_begin = date_tutoring_begin
        self.address = address
        self.id_region = id_region

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO репетиторы (Имя, Фамилия, Отчество, email, Мобильный_телефон, Дата_рождения, Дата_начала_преподавания, Адрес, регионы_ID_региона) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (self.name, self.surname, self.patronymic, self.email, self.tel,  self.birth_date,  self.date_tutoring_begin, self.address, self.id_region))
        self.db_connection.commit()
        c.close()


class TutorsEducation:
    def __init__(self, db_connection, id_tutor, id_education):
        self.db_connection = db_connection.connection
        self.id_tutor = id_tutor
        self.id_education = id_education

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO репетиторы_образование (репетиторы_ID_репетитора, образование_ID_образования) VALUES (%s, %s);", (self.id_tutor, self.id_education))
        self.db_connection.commit()
        c.close()


class TutorsSubjects:
    def __init__(self, db_connection, id_tutor, id_subject):
        self.db_connection = db_connection.connection
        self.id_tutor = id_tutor
        self.id_subject = id_subject

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO репетиторы_предметы (репетиторы_ID_репетитора, предметы_ID_предмета) VALUES (%s, %s);", (self.id_tutor, self.id_subject))
        self.db_connection.commit()
        c.close()


con = Connection(user='dbuser', password='123', db='tutoring')

# with con:
    # tutedu = TutorsEducation(con, '1', '1')
    # tutedu.save()
    # sub = Subjects(con, 'Математика')
    # sub.save()
    # tutsub = TutorsSubjects(con, '1', '1')
    # tutsub.save()
    # tut = Tutors(con, 'Петр', 'Петров', 'Петрович', 'ivanov@mail.ru', '89992223344', '1970.01.01', '1999.01.01', 'Baker St. 22', '1')
    # tut.save()
    # edu = Education(con, 'МГУ')
    # edu.save()
    # reg = Regions(con, 'Москва')
    # reg.save()



