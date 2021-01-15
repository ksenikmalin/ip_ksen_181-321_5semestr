from django.db import models

class Сlient(models.Model):
    surname = models.CharField("Фамилия", max_length=150)
    name = models.CharField("Имя", max_length=150)
    patronymic = models.CharField("Отчество", max_length=150)
    number_phone = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Электронная почта", max_length=255)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Order_status(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
       
    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"


class Object(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
       
    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

class Repair_type(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
    cost_of_work = models.IntegerField("Стоимость вида работы за кв/м")   
    type_of_work = models.CharField("Производимые работы", max_length=510)
    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Виды работы"



class Duration(models.Model):
    amount_of_days = models.CharField("Количетво дней от/до", max_length=150)
       
    def __str__(self):
        return self.amount_of_days

    class Meta:
        verbose_name = "Продолжительность"
        verbose_name_plural = "Продолжительности"

class Services(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
   
    id_repair_type = models.ForeignKey(Repair_type, verbose_name="Вид работы", on_delete=models.SET_NULL, null=True)
    id_object = models.ForeignKey(Object, verbose_name="Объект", on_delete=models.SET_NULL, null=True)
    id_duration = models.ForeignKey(Duration, verbose_name="Продолжительность", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Files(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
    image = models.ImageField("Изображение", upload_to="media/", null=True)
 
    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Order(models.Model):
    start_date = models.DateTimeField 
    end_date = models.DateTimeField
    address = models.CharField("Адрес", max_length=150)
    square = models.CharField("Площадь", max_length=150)
    price = models.IntegerField("Цена")
    comment = models.TextField("Комментарий")
    
    id_client = models.ForeignKey(Сlient, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)
    id_order_status = models.ForeignKey(Order_status, verbose_name="Статус заказа", on_delete=models.SET_NULL, null=True)
    id_services = models.ForeignKey(Services, verbose_name="Услуга", on_delete=models.SET_NULL, null=True)
 
    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class Portfolio(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание")

    id_files = models.ForeignKey(Files, verbose_name="Файл", on_delete=models.SET_NULL, null=True)
    id_order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолия"

class Reviews(models.Model):
    text = models.CharField("текст", max_length=250)

    id_client = models.ForeignKey(Сlient, verbose_name="Клиент", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Call_application_status(models.Model):
    naimenovaniye = models.CharField("Наименование", max_length=150)
 
    def __str__(self):
        return self.naimenovaniye

    class Meta:
        verbose_name = "Статус заявки на обратный звонок"
        verbose_name_plural = "Статусы заявок на обратный звонок"

class Back_call(models.Model):
    name = models.CharField("Имя", max_length=150)
    number_phone = models.CharField("Номер телефона", max_length=20)
        
    id_call_application_status = models.ForeignKey(Call_application_status, verbose_name="Статус заявки на обратный звонок", on_delete=models.SET_NULL, null=True)
   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратный звонок"
        verbose_name_plural = "Обратные звонки"

