from django.contrib import admin

from .models import Tenant, TenantAwareModel

admin.site.register(Tenant)
#admin.site.register(TenantAwareModel)
