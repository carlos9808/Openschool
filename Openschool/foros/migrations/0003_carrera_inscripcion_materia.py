# Generated by Django 2.0.3 on 2018-04-04 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_usuarios_perfil'),
        ('foros', '0002_articulo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Carrera', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Carrera')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cuentas.Usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Materia', models.CharField(max_length=200)),
                ('Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foros.Carrera')),
            ],
        ),
    ]