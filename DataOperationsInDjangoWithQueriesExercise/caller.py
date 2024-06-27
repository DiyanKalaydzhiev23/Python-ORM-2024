import os
import django
from django.db.models import QuerySet, F

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.core.management import call_command

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character
from populate_db_script import populate_model_with_data


# call_command('makemigrations')
# call_command('migrate')


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name)
    # UPDATE artefact SET name = new_name WHERE is_magical=TRUE && age > 250 && id = 1

    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return "\n".join(str(l) for l in locations)


def new_capital() -> None:
    # Location.objects.filter(id=1).update(is_capital=True)

    location = Location.objects.first()  # SELECT * FROM locations LIMIT 1
    location.is_capital = True
    location.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year)) / 100  # 2014 => 2 + 0 + 1 + 4 => 7 / 100 => 0.07
        discount = float(car.price) * percentage_off  # 1000 * 0.07 => 70
        car.price_with_discount = float(car.price) - discount  # 1000 - 70 => 930
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return "\n".join(str(t) for t in unfinished_tasks)


def complete_odd_tasks() -> None:
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)

    # Option 2 - worse
    # tasks_with_matching_title = Task.objects.filter(title=task_title)
    #
    # for task in tasks_with_matching_title:
    #     task.description = decoded_text
    #
    # Task.objects.bulk_update(tasks_with_matching_title, ['description'])


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]

    return "\n".join(even_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')  # id 1, id 2...

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name="Mage").update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name="Warrior").update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )
    # UPDATE table
    # SET
    #   intelligence = intelligence - 7,
    #   level = level + 3
    # WHERE class_name IN ("Assassin", "Scout")


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + " " + second_character.name
    class_name = "Fusion"
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = first_character.hit_points + second_character.hit_points

    if first_character.class_name in ["Mage", "Scout"]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()
