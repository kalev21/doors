# Generated by Django 3.2.8 on 2021-12-04 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Коллекция')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('hours', models.TextField(max_length=300, verbose_name='Часы работы')),
                ('site', models.CharField(max_length=20, verbose_name='Сайт')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='DeliverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Доставка')),
                ('up_text', models.CharField(max_length=50, verbose_name='Подъём')),
                ('up_text_1', models.CharField(max_length=50, verbose_name='Подъём')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставка',
            },
        ),
        migrations.CreateModel(
            name='FeedBackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('publish_date', models.DateTimeField(auto_now=True, verbose_name='Время публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='ProductsCardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование товара')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='URL')),
                ('image', models.ImageField(default=None, upload_to='img', verbose_name='Карточка товара')),
                ('description', models.TextField(max_length=300, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена продукта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
