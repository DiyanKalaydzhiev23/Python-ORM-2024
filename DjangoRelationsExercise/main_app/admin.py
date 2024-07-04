from django.contrib import admin
from main_app.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "year", "owner", "car_details"]

    @staticmethod
    def car_details(car: Car) -> str:
        try:
            owner = car.owner.name
        except AttributeError:
            owner =  "No owner"

        try:
            registration = car.registration.registration_number
        except AttributeError:
            registration = "No registration number"

        return f"Owner: {owner}, Registration: {registration}"

    car_details.short_description = "Car Details"
