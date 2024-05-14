import csv
from datetime import datetime

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vicaima.settings')
application = get_wsgi_application()
from evals.models import Colaboradores

def import_colab(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Colaboradores.objects.create(
				colaborador_id=row['Nº colaborador'],
				name=row['Nome'],
				last_name=row['Apelido'],
				department=row['Departamento'],
				function=row['Função'],
				admission_date=datetime.strptime(row['Data de Admissão'], '%d/%m/%Y').date(),
				functional_group=row['Grupo Funcional:']
            )

if __name__ == '__main__':
    csv_file_path = 'colaboradores.csv'
    import_colab(csv_file_path)