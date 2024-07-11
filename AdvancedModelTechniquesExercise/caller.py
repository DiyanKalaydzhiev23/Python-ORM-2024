import os
from decimal import Decimal

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Document

from django.contrib.postgres.search import SearchVector

results = Document.objects.filter(search_vector='django web framework')

for result in results:
    print(f"Title: {result.title}")
