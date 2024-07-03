# Python-ORM-2024

# Important commands

### Zip project on Mac/Linux
```bash
   zip -r project.zip . -x "*.idea*" -x "*venv*" -x "*__pycache__*"
```

---

### Zip project on Windows
```bash
   tar.exe -a -cf project.zip main_app orm_skeleton caller.py manage.py requirements.txt
```

---

### Creation of Venv
```bash
	python3 -m venv ./venv
	source ./venv/bin/activate
	venv\Scripts\activate
```

---

### dbshell on Docker

```bash
	docker exec -t <container_name> /bin/bash
	psql -U your_user_me -d your_db_name
```

---

# Helpers

- [Populate Django DB Script](https://github.com/DiyanKalaydzhiev23/PopulateDjangoModel)

# Theory Tests

---

- [Django Models Basics](https://forms.gle/JwTbUtEkddw2Kc2R7)

---

- [Migrations and Django Admin](https://forms.gle/7G2KzMujkCzHDgPb8)

---

- [Data Operations with Django Queries](https://forms.gle/Pzay1RHaUuQCb1X68)

---

- [Working with Queries](https://forms.gle/kieTF55zwmK2eAaM7)

---

- [Django Relations](https://forms.gle/6uvQdwzqfxt87kD36)

---

# Plans

--- 

### Django Models

```
ORM - Object Relational Mapping
```

0. ORM - Предимства и недостатъци
   - Pros:
     -  Не ни се налага писането на low level SQL
     -  По-лесна поддръжка
     -  Добър при CRUD операции
   - Cons:
     - Не много оптимизиран за по-сложни заявки
     - Възможно е да влага излишна сложност в някои от заявките

2. Django models
   - Всеки модел е отделна таблица
   - Всяка променлова използваща поле от `models` е колона в тази таблица

3. Създаване на модели
   - Наследяваме `models.Model`
    

4. Migrations
   - `makemigrations` - създава миграции
   - `migrate` - прилага миграциите
  
5. Други команди
   - `dbshell` - отваря конзола, в която можем да пишем SQL
   - `CTRL + ALT + R` - отваря manage.py console

---

### Migrations and Admin

1. Django Migrations Advanced
   - Миграциите ни помагат надграждаме промени в нашите модели
   - Както и да можем да пазим предишни стейтове на нашата база
   - Команди:
     - makemigrations
     - migrate
     - Връщане до определена миграция - migrate main_app 0001
     - Връщане на всички миграции - migrate main_app zero
     - showmigrations - показва всички апове и миграциите, които имат
     - showmigrations app_name - показва миграциите за един app
     - showmigrations --list - showmigrations -l 
     - squashmigrations app_name migration_to_which_you_want_to_sqash - събира миграциите до определена миграция в една миграция
     - sqlmigrate app_name migration_name - дава ни SQL-а на текущата миграция - използваме го, за да проверим дали миграцията е валидна
     - makemigrations --empty main_app - прави празна миграция в зададен от нас app

2. Custom/Data migrations
   - Когато например добавим ново поле, искаме да го попълним с данни на база на вече съществуващи полета, използваме data migrations
   - RunPython
     - викайки функция през него получаваме достъп до всички апове и техните модели (първи параметър), Scheme Editor (втори параметър)
     - добра практика е да подаваме фунцкия и reverse функция, за да можем да връяа безпроблемно миграции
   - Scheme Editor - клас, който превръща нашия пайтън код в SQL, ползваме го когато правим create, alter и delete на таблица
     - използвайки RunPython в 95% от случаите няма да ни се наложи да ползавме Scheme Editor, освен, ако не правим някаква временна таблица
       индекси или промяна на схемата на таблицата
   - Стъпки:
     
      2.1. Създаваме празен файл за миграция: makemigrations --empty main_app - прави празна миграция в зададен от нас app
      
      2.2. Дефиниране на операции - Използваме RunPython за да изпълним data migrations
      
      2.3. Прилагане на промените - migrate

Пример с временна таблица:

Да приемем, че имате модел с име „Person“ във вашето Django приложение и искате да създадете временна таблица, за да съхранявате някои изчислени данни въз основа на съществуващите данни в таблицата „Person“. 
В този случай можете да използвате мигриране на данни, за да извършите тази операция:

1. **Create the Data Migration:**

Run the following command to create a data migration:

```bash
python manage.py makemigrations your_app_name --empty
```

This will create an empty data migration file.

2. **Edit the Data Migration:**

Open the generated data migration file and modify it to use `RunPython` with a custom Python function that utilizes the `SchemaEditor` to create a temporary table. Here's an example:

```python
from django.db import migrations, models

def create_temporary_table(apps, schema_editor):
    # Get the model class
    Person = apps.get_model('your_app_name', 'Person')

    # Access the SchemaEditor to create a temporary table
    schema_editor.execute(
        "CREATE TEMPORARY TABLE temp_person_data AS SELECT id, first_name, last_name FROM your_app_name_person"
    )

def reverse_create_temporary_table(apps, schema_editor):
    schema_editor.execute("DROP TABLE temp_person_data")

class Migration(migrations.Migration):

    dependencies = [
        ('your_app_name', 'previous_migration'),
    ]

    operations = [
        migrations.RunPython(create_temporary_table, reverse_create_temporary_table),
    ]
```

3. Django admin
   - createsuperuser
   - Register model, example:
   
   ```python
      @admin.register(OurModelName)
      class OurModelNameAdmin(admin.ModelAdmin):
   	pass
   ```
4. Admin site customizations
  - __str__ метод в модела, за да го визуализираме в админ панела по-достъпно

  - list_display - Показваме различни полета още в админа
    Пример: 
    ```python
    class EmployeeAdmin(admin.ModelAdmin):
    	list_display = ['job_title', 'first_name', 'email_address']
    ```

  - List filter - добавя страничен панел с готови филтри
    Пример:

      ```python
       class EmployeeAdmin(admin.ModelAdmin):
       	list_filter = ['job_level']
      ```

  - Searched fields - казваме, в кои полета разрешаваме да се търси, по дефолт са всички
    Пример:
    
    ```python
    class EmployeeAdmin(admin.ModelAdmin):
        search_fields = ['email_address']
    ```
  
  - Layout changes - избираме, кои полета как и дали да се появяват при добавяне или промяна на запис
    Пример:
    
    ```python
    class EmployeeAdmin(admin.ModelAdmin):
        fields = [('first_name', 'last_name'), 'email_address']
    ```

  - list_per_page
   
  - fieldsets - променяме визуално показването на полетата
    Пример:
    ```python
      fieldsets = (
           ('Personal info',
            {'fields': (...)}),
           ('Advanced options',
            {'classes': ('collapse',),
           'fields': (...),}),
      )
    ```

---

### Data Operations in Django with queries


1. CRUD overview
   - CRUD - Create, Read, Update, Delete
   - Използваме го при: 
     - Web Development
     - Database Management
   - Дава ни един консистентен начин, за това ние да създаваме фунцкионалност за CRUD
   - Можем да го правим през ORM-a на Джанго

2. Мениджър в Django:
    - Атрибут на ниво клас на модел за взаимодействия с база данни.
    - Отговорен за CRUD
    - Custom Manager: Подклас models.Model.
       - Защо персонализирани мениджъри:
         - Капсулиране на общи или сложни заявки.
         - Подобрена четимост на кода.
         - Избягвайме повторенията и подобряваме повторната употреба.
         - Промяна наборите от заявки според нуждите.

3. Django Queryset
   - QuerySet - клас в пайтън, които изпозваме, за да пазим данните от дадена заявка
   - Данните не се взимат, докато не бъдат потърсени от нас
   - cars = Cars.objects.all() # <QuerySet []>
   - print(cars)  # <QuerySet [Car object(1)]>

   - QuerySet Features: 
     - Lazy Evaluation - примера с колите, заявката не се вика, докато данните не потрябват
     - Retrieving objects - можем да вземаме всички обекти или по даден критерии
     - Chaining filters - MyModel.objects.filter(category='electronics').filter(price__lt=1000)
     - query related objects - позволява ни да търсим в таблици, с които имаме релации, през модела: # Query related objects using double underscores
related_objects = Order.objects.filter(customer__age__gte=18)
     - Ordering - ordered_objects = Product.objects.order_by('-price')
     - Pagination 
      ```python
       from django.core.paginator import Paginator

        # Paginate queryset with 10 objects per page
        paginator = Paginator(queryset, per_page=10)
        page_number = 2
        print([x for x in paginator.get_page(2)])
      ```

4. Django Simple Queries
   - Object Manager - default Objects
   - Methods:
     - `all()`
     - `first()`
     - `get(**kwargs)`
     - `create(**kwargs)`
     - `filter(**kwargs)`
     - `order_by(*fields)`
     - `delete()`

5. Django Shell and SQL Logging
   - Django Shell
     - Дава ни достъп до целия проект
     - python manage.py shell
   - SQL logging
     -  Enable SQL logging

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',  # Other levels CRITICAL, ERROR, WARNING, INFO, DEBUG
    },
    'loggers': {
        'django.db.backends': {  # responsible for the sql logs
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

---

### Working with queries


1. Useful Methods
   - filter() - връща subset от обекти; приема kwargs; връща queryset;
   - exclude() - връща subset от обекти; приема kwargs; връща queryset;
   - order_by() - връща сортираните обекти; - за desc;
   - count() - като len, но по-бързо; count връща само бройката без да му трябвата реалните обекти;
   - get() - взима един обект по даден критерии;


2. Chaning methods
   - всеки метод работи с върнатия от предишния резултат


3. Lookup keys
   - Използват се във filter, exclude, get;
   - __exact __iexact - матчва точно;
   - __contains __icontains - проверява дали съдържа;
   - __startswith __endswith
   - __gt __gte
   - __lt __lte
   - __range=(2, 5) - both inclusive

4. Bulk methods
   - използват се, за да извършим операции върху много обекти едновременно
   - bulk_create - създава множество обекти навъеднъж;
   - filter().update()
   - filter().delete()

---


###  Django Relations

Django Models Relations


1. Database Normalization
   - Efficient Database Organization
     - Data normalization - разбива големи таблици на по-малки такива, правейки данните по-организирани
     - Пример: Все едно имаме онлайн магазин и вместо да пазим име, адрес и поръчка в една таблица, можем да разбием на 3 таблици и така да не повтаряме записи
   
    - Guidelines and Rules
      - First Normal Form
      	- First Normal Form (1NF): елеминираме поврарящите се записи, всяка таблица пази уникални стойности

        - Second Normal Form (2NF): извършваме първото като го правим зависимо на PK
          - Пример: Онлайн магазин с данни и покупки Customers и Orders са свързани с PK, вместо всичко да е в една таблица

	- Third Normal Form (3NF):
          - премахване на преходни зависимости
          - Таблица служители пази id, служител, град, адрес => разделяме ги на 3 таблици и ги навързваме, без да е задължително по PK, може и по city_id вече employee е независимо
        
        - Boyce-Codd Normal Form (BCNF):
          - По-строга версия на 3NF
          - Тук правим да се навързват по PK

	 - Fourth Normal Form (4NF):
          - Ако данни от една таблица се използват в други две то това не е добре
          - Пример: Имаме Курс X и Курс Y, на X Му трябват книгите A и B, на Y, A и C,
            това, което правим е да направим таблица с книгите А и таблица с Книгите Б
         
         - Fifth Normal Form (5NF) - Project-Join Normal Form or PJ/NF:
           - Кратко казано да не ни се налага да минаваме през таблици с данни, които не ни трябват, за да достигнем до таблица с данни, която ни трябва

   - Database Schema Design
      - Създаването на различни ключове и връзки между таблиците

   - Minimizing Data Redundancy
     - Чрез разбиването на таблици бихме имали отново намалено повтаряне на информация
     - Имаме книга и копия, копията са в отделна таблица, и са линкнати към оригинала
   
   - Ensuring Data Integrity & Eliminating Data Anomalies
     - Това ни помага да update-ваме и изтриваме данните навсякъде еднакво
     - отново благодарение на някакви constraints можем да променим една стойност в една таблица и тя да се отрази във всички

   - Efficiency and Maintainability
     - Благодарение на по-малките таблици, ги query–ваме и update-ваме по-бързо

2. Релации в Django Модели
   - Получават се използвайки ForeignKey полета
   - related_name - можем да направим обартна връзка
     - По дефолт тя е името + _set
  
   - Пример:
   ```py
   class Author(models.Model):
       name = models.CharField(max_length=100)
   
   class Post(models.Model):
       title = models.CharField(max_length=200)
       content = models.TextField()
       author = models.ForeignKey(Author, on_delete=models.CASCADE)
   ```

- Access all posts written by an author
```py
author = Author.objects.get(id=1)
author_posts = author.post_set.all()
```

3. Types of relationships
   - Many-To-One (One-To-Many)
   - Many-To-Many 
     - Няма значение, в кой модел се слага
     - Django автоматично създава join таблица или още наричана junction
     - Но, ако искаме и ние можем да си създадем: 
      ```py
      class Author(models.Model):
          name = models.CharField(max_length=100)
      
      class Book(models.Model):
          title = models.CharField(max_length=200)
          authors = models.ManyToManyField(Author, through='AuthorBook')
      
      class AuthorBook(models.Model):
          author = models.ForeignKey(Author, on_delete=models.CASCADE)
          book = models.ForeignKey(Book, on_delete=models.CASCADE)
          publication_date = models.DateField()
      ```

   - OneToOne, предимно се слага на PK
   - Self-referential Foreign Key
      - Пример имаме работници и те могат да са мениджъри на други работници
        
   ```py
   class Employee(models.Model):
       name = models.CharField(max_length=100)
       supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
   ```

    - Lazy Relationships - обекта от релацията се взима, чрез заявка, чак когато бъде повикан

---
