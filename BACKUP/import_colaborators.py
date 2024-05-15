import csv
from datetime import datetime
from django.db import connection, transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vicaima.settings')
application = get_wsgi_application()
from evals.models import Colaboradores

def import_colab(file_path):
    Colaboradores.objects.all().delete()
    User.objects.all().delete()  # Delete all User instances
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = '" + Colaboradores._meta.db_table + "'")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = '" + User._meta.db_table + "'")  # Reset User ID sequence
        transaction.commit()
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nickname = row['Nome'] + " " + row['Apelido']
            Colaboradores.objects.create(
                nickname=nickname,
                name=row['Nome'],
                last_name=row['Apelido'],
                department=row['Departamento'],
                function=row['Função'],
                admission_date=datetime.strptime(row['Data de Admissão'], '%d/%m/%Y').date(),
                functional_group=row['Grupo Funcional:'],
                password=""
            )
            User.objects.create_user(  # Create a User instance
                username=nickname,
                password="",
                first_name=row['Nome'],
                last_name=row['Apelido'],
            )

if __name__ == '__main__':
    csv_file_path = 'colaboradores.csv'
    import_colab(csv_file_path)