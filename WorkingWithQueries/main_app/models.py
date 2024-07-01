from django.db import models

from main_app.choices import LaptopBrandChoice, OperationSystemChoice, MealTypeChoice, DungeonDifficultyChoice, \
    WorkoutTypeChoice


class ArtworkGallery(models.Model):
    artist_name = models.CharField(
        max_length=100,
    )

    art_name = models.CharField(
        max_length=100,
    )

    rating = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class Laptop(models.Model):
    brand = models.CharField(
        max_length=20,
        choices=LaptopBrandChoice.choices
    )

    processor = models.CharField(
        max_length=100,
    )

    memory = models.PositiveIntegerField(
        help_text="Memory in GB",
    )

    storage = models.PositiveIntegerField(
        help_text="Storage in GB",
    )

    operation_system = models.CharField(
        max_length=20,
        choices=OperationSystemChoice.choices,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class ChessPlayer(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True
    )

    title = models.CharField(
        max_length=100,
        default="no title"
    )

    rating = models.PositiveIntegerField(
        default=1500
    )

    games_played = models.PositiveIntegerField(
        default=0
    )

    games_won = models.PositiveIntegerField(
        default=0
    )

    games_lost = models.PositiveIntegerField(
        default=0
    )

    games_drawn = models.PositiveIntegerField(
        default=0
    )


class Meal(models.Model):
    name = models.CharField(
        max_length=100
    )

    meal_type = models.CharField(
        max_length=10,
        choices=MealTypeChoice.choices
    )

    preparation_time = models.CharField(
        max_length=30
    )

    difficulty = models.PositiveIntegerField()

    calories = models.PositiveIntegerField()

    chef = models.CharField(
        max_length=100
    )


class Dungeon(models.Model):
    name = models.CharField(
        max_length=100
    )

    difficulty = models.CharField(
        max_length=10,
        choices=DungeonDifficultyChoice.choices
    )

    location = models.CharField(
        max_length=100
    )

    boss_name = models.CharField(
        max_length=100
    )

    recommended_level = models.PositiveIntegerField()

    boss_health = models.PositiveIntegerField()

    reward = models.TextField()

    def __str__(self):
        return f"{self.name} is guarded by {self.boss_name} who has {self.boss_health} health points!"


class Workout(models.Model):
    name = models.CharField(
        max_length=200
    )

    workout_type = models.CharField(
        max_length=20,
        choices=WorkoutTypeChoice.choices
    )

    duration = models.CharField(
        max_length=30
    )

    difficulty = models.CharField(
        max_length=50
    )

    calories_burned = models.PositiveIntegerField()

    instructor = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.name} from {self.workout_type} type has {self.difficulty} difficulty!"
