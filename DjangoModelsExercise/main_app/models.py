from django.db import models

# Creating venv
# python3 -m venv ./venv
# for mac source ./venv/bin/activate
# for windows venv\Scripts\activate


class Person(models.Model):
    name = models.CharField(
        max_length=30
    )

    age = models.PositiveIntegerField()


class Blog(models.Model):
    post = models.TextField()

    author = models.CharField(
        max_length=35,
    )


class WeatherForecast(models.Model):
    date = models.DateField()  # DATE

    temperature = models.FloatField()

    humidity = models.FloatField()

    precipitation = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField()

    ingredients = models.TextField()

    cook_time = models.PositiveIntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Product(models.Model):
    name = models.CharField(
        max_length=70,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )  # NUMERIC/DECIMAL(10, 2)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class UserProfile(models.Model):
    username = models.CharField(
        max_length=65,
        unique=True
    )

    first_name = models.CharField(
        max_length=40,
    )

    last_name = models.CharField(
        max_length=40,
    )

    email = models.EmailField(
        unique=True,
        default="students@softuni.bg",
    )

    bio = models.TextField(
        max_length=120,
    )

    profile_image_url = models.URLField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    duration_minutes = models.PositiveIntegerField()

    difficulty_level = models.CharField(
        max_length=20,
    )

    equipment = models.CharField(
        max_length=90,
    )

    video_url = models.URLField(
        null=True,
        blank=True,
    )

    calories_burned = models.PositiveIntegerField(
        default=1,
    )

    is_favorite = models.BooleanField(
        default=False,
    )


class GenreChoices(models.TextChoices):
    FICTION = "Fiction", "Fiction"
    NON_FICTION = "Non-Fiction", "Non-Fiction"
    SCIENCE_FICTION = "Science Fiction", "Science Fiction"
    HORROR = "Horror", "Horror"


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )

    author = models.CharField(
        max_length=100,
    )

    genre = models.CharField(
        max_length=20,
        choices=GenreChoices.choices
    )

    publication_date = models.DateField(
        editable=False,
        auto_now_add=True,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    is_available = models.BooleanField(
        default=True,
    )

    rating = models.FloatField()

    description = models.TextField()

    def __str__(self):
        return self.title

