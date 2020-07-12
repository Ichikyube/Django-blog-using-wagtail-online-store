from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import GuestEmail, EmailActivation

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm #editView
    add_form = UserAdminCreationForm #createView

    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
       # ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff', 'is_active')})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class EmailActivationAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = EmailActivation


admin.site.register(EmailActivation, EmailActivationAdmin)

class GuestEmailAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = GuestEmail
admin.site.register(GuestEmail, GuestEmailAdmin)