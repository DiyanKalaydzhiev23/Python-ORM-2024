import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import CreditCard

# Create CreditCard instances with card owner names and card numbers
credit_card1 = CreditCard(card_owner="Krasimir", card_number="123456789012345424234572357423570")
credit_card2 = CreditCard(card_owner="Pesho", card_number="9876543210987654")
credit_card3 = CreditCard(card_owner="Vankata", card_number="45678901234567894")

CreditCard.objects.filter()

# Save the instances to the database
credit_card1.save()
credit_card2.save()
credit_card3.save()

# Retrieve the CreditCard instances from the database
credit_cards = CreditCard.objects.all()
# Display the card owner names and masked card numbers
for credit_card in credit_cards:
    print(f"Card Owner: {credit_card.card_owner}")
    print(f"Card Number: {credit_card.card_number}")
