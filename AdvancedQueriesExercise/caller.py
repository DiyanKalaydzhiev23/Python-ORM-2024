import os
from datetime import date

import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing, VideoGame, BillingInfo, Invoice, Project, Programmer, Technology, Task
