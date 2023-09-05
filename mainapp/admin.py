from django.contrib import admin
from django.contrib.auth.models import Group , User 
from .models import Profile , Twieet , Supplier , Shipping , Sticker , Cartoon , OilSupplier
# Register your models here.

admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Twieet)
admin.site.register(Supplier)
admin.site.register(Shipping)
admin.site.register(Sticker)
admin.site.register(Cartoon)
admin.site.register(OilSupplier)

