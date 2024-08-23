from django.contrib import admin
from contact import models
# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    # Show id, first_name, last_name, phone in http://127.0.0.1:8000/admin/contact/contact/
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)

    # Contact will ordered by "-ID" descending
    ordering = ('-id',)

    # Contact can be searched by first_name
    search_fields = ('first_name',)

    # How many contacts will i show for page and max contacts to show options "show all"
    list_per_page = 10
    list_max_show_all = 100

    # Editable contact without accessing the contact
    list_editable = ('first_name', 'last_name', 'phone', 'show',)

    # Where will the access link be located
    list_display_links = ('id',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    ordering = ('-id',)
