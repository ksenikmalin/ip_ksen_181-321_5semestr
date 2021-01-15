from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from .models import Сlient, Order_status, Object, Repair_type, Duration, Services, Files, Portfolio, Reviews, Order, Back_call, Call_application_status


@admin.register(Сlient)
class СlientAdmin(ImportExportModelAdmin):
    list_display = ("surname", "name", "patronymic", "number_phone", "email")
    pass


@admin.register(Order_status)
class Order_statusAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye",)
    pass

@admin.register(Object)
class ObjectAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye",)
    pass

@admin.register(Repair_type)
class Repair_typeAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye", "cost_of_work", "type_of_work")
    pass
  

@admin.register(Duration)
class DurationAdmin(ImportExportModelAdmin):
    list_display = ("amount_of_days",)
    pass

@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye", "id_repair_type", "id_object", "id_duration")
    pass

@admin.register(Files)
class FilesAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye", "image")
    pass

@admin.register(Portfolio)
class PortfolioAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye", "description", "id_files", "id_order")
    pass

@admin.register(Reviews)
class ReviewsAdmin(ImportExportModelAdmin):
    list_display = ("text", "id_client")
    pass

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ("start_date", "end_date", "address", "square", "price", "comment", "id_client", "id_order_status", "id_services")
    pass

@admin.register(Back_call)
class Back_callAdmin(ImportExportModelAdmin):
    list_display = ("name", "number_phone", "id_call_application_status")
    pass

@admin.register(Call_application_status)
class Call_application_statusAdmin(ImportExportModelAdmin):
    list_display = ("naimenovaniye",)
    pass
