from django.contrib import admin
from .models import Child, VaccinationRecord
# vaccination/admin.py

from django.contrib import admin
from .models import Child, VaccinationRecord

class VaccinationRecordAdmin(admin.ModelAdmin):
    list_display = ('child', 'vaccine_type', 'dose_number', 'date_administered')
    search_fields = ('child__full_name', 'vaccine_type')

    # Customize the form to allow parent and child selection
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "child":
            # Limit the queryset to only show children of registered parents
            kwargs["queryset"] = Child.objects.filter(parent__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register the models with the admin site
admin.site.register(Child)
admin.site.register(VaccinationRecord, VaccinationRecordAdmin)



