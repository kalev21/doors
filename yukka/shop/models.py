from django.db import models


class FeedBackModel(models.Model):  # Модель отзывов
    author = models.CharField('Имя', max_length=30)
    text = models.TextField('Текст отзыва')
    publish_date = models.DateTimeField('Время публикации', auto_now=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ProductsCardModel(models.Model):
    name = models.CharField('Наименование товара', max_length=30)
    slug = models.SlugField('URL', max_length=30, unique=True, db_index=True)
    image = models.ImageField('Карточка товара', upload_to='img', default=None)
    description = models.TextField('Описание товара', max_length=300)
    price = models.IntegerField('Цена продукта')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # CASCADE удаляет все карточки в категории

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField('Коллекция', max_length=30, unique=True)
    slug = models.SlugField('URL', max_length=30, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class ContactModel(models.Model):
    address = models.TextField('Адрес', max_length=100)
    phone = models.CharField('Телефон', max_length=12)
    hours = models.TextField('Часы работы', max_length=300)
    site = models.CharField('Сайт', max_length=20)
    email = models.EmailField('Email')

    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class DeliverModel(models.Model):
    text = models.CharField('Доставка', max_length=100)
    up_text = models.CharField('Подъём', max_length=50)
    up_text_1 = models.CharField('Подъём', max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'