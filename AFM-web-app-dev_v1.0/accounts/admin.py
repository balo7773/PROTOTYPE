from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import SignUpForm  # Ensure you import your form here if needed
from .models import CustomUser

try:
    admin.site.unregister(CustomUser)
except admin.sites.NotRegistered:
    pass  # Ignore error if CustomUser is not registered

# Now register CustomUser with the default UserAdmin
admin.site.register(CustomUser, UserAdmin)


'''class CustomUserAdmin(UserAdmin):
    model = User
    # Include other fields you want to display in the list view
    list_display = ('username',
                    'email',
                    'age',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                    'date_joined')
    
    # Add the fields you want to show/edit in the form view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    # Add the age field to the add form if you're customizing
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )'''
