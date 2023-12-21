#!/usr/bin/env python
# coding: utf-8

# In[1]:

from django.http import JsonResponse
from django.views import View
from .models import DatabaseAModel, DatabaseCModel

# In[2]:

class DatabaseAView(View):
    def get(self, request, *args, **kwargs):
        data_a = DatabaseAModel.objects.values()
        return JsonResponse(list(data_a), safe=False)

# In[3]:

class DatabaseCView(View):
    def get(self, request, *args, **kwargs):
        data_c = DatabaseCModel.objects.values()
        return JsonResponse(list(data_c), safe=False)

# In[4]:

class CombinedDataView(View):
    def get(self, request, *args, **kwargs):
        combined_data = []

        data_a = DatabaseAModel.objects.all()

        for entry_a in data_a:
            foreign_key_a = entry_a.foreign_key
            entry_c = DatabaseCModel.objects.filter(foreign_key=foreign_key_a).first()

            if entry_c:
                combined_entry = {
                    'name': entry_a.name,
                    'number': entry_a.number,
                    'age': entry_a.age,
                    'foreign_key': entry_a.foreign_key,
                    'email': entry_c.email,
                    'address': entry_c.address
                }
                combined_data.append(combined_entry)

        return JsonResponse(combined_data, safe=False)
