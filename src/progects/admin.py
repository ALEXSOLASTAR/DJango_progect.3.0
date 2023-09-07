from django.contrib import admin

from progects.models import Progect


class ProgectAdmin(admin.ModelAdmin):

    class Meta:
        model = Progect

    list_display = ("name", "from_language", "to_language", "progect_progres")
    list_editable = ("progect_progres", )


admin.site.register(Progect, ProgectAdmin)
