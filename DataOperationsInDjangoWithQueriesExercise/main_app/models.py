from django.db import models


class CustomManager(models.Manager):
    def really_complex_query(self):
        return "Really complex query"


class MyModel(models.Model):
    field1 = models.CharField(
        max_length=100,
    )


class Pet(models.Model):
    name = models.CharField(
        max_length=40,
    )

    species = models.CharField(
        max_length=40,
    )


class Artifact(models.Model):
    name = models.CharField(
        max_length=70,
    )

    origin = models.CharField(
        max_length=70,
    )

    age = models.PositiveIntegerField()

    description = models.TextField()

    is_magical = models.BooleanField(
        default=False
    )


class Location(models.Model):
    name = models.CharField(
        max_length=100,
    )

    region = models.CharField(
        max_length=50,
    )

    population = models.PositiveIntegerField()

    description = models.TextField()

    is_capital = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.name} has a population of {self.population}!"


class Car(models.Model):
    model = models.CharField(
        max_length=40,
    )

    year = models.PositiveIntegerField()

    color = models.CharField(
        max_length=40,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    price_with_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


class Task(models.Model):
    title = models.CharField(
        max_length=25,
    )

    description = models.TextField()

    due_date = models.DateField()

    is_finished = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Task - {self.title} needs to be done until {self.due_date}!"


class RoomTypeChoices(models.TextChoices):
    STANDARD = "Standard", "Standard"
    DELUXE = "Deluxe", "Deluxe"
    SUITE = "Suite", "Suite"


class HotelRoom(models.Model):
    room_number = models.PositiveIntegerField()

    room_type = models.CharField(
        max_length=10,
        choices=RoomTypeChoices.choices
    )

    capacity = models.PositiveIntegerField()

    amenities = models.TextField()

    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    is_reserved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.room_type} room with number {self.room_number} costs {self.price_per_night}$ per night!"


class CharacterChoices(models.TextChoices):
    MAGE = "Mage", "Mage"
    WARRIOR = "Warrior", "Warrior"
    ASSASSIN = "Assassin", "Assassin"
    SCOUT = "Scout", "Scout"


class Character(models.Model):
    name = models.CharField(
        max_length=100,
    )

    class_name = models.CharField(
        max_length=20,
        choices=CharacterChoices.choices
    )

    level = models.PositiveIntegerField()

    strength = models.PositiveIntegerField()

    dexterity = models.PositiveIntegerField()

    intelligence = models.PositiveIntegerField()

    hit_points = models.PositiveIntegerField()

    inventory = models.TextField()
