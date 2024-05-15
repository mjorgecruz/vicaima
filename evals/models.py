from django.db import models

class Colaboradores(models.Model):
	nickname = models.CharField(max_length=200)
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	function = models.CharField(max_length=100)
	admission_date = models.DateField()
	functional_group = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	
# class Correlacoes(models.Model):
# 	colaborador_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
# 	evaluator_id = models.ForeignKey(Colaboradores.colaborador_id, on_delete=models.CASCADE)
# 	director_id = models.ForeignKey(Colaboradores.colaborador_id, on_delete=models.CASCADE)

class Eventos(models.Model):
	creation_date = models.DateField()
	deadline = models.DateField()
	evaluator_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
	evaluation_status = models.BooleanField(default=False)
	def __str__(self):
		return self.name
	
class Avaliados(models.Model):
	id = models.AutoField(primary_key=True)
	evaluation_id = models.ForeignKey(Eventos, on_delete=models.CASCADE)
	evaluated_id = models.ManyToManyField(Colaboradores)
	def __str__(self):
		return self.name

class Resultados(models.Model):
	result_id = models.ForeignKey(Avaliados, on_delete=models.CASCADE)
	result = models.IntegerField(default=0)
	classification = models.CharField(max_length=1, default='D')

class Form(models.Model):
	form = models.CharField(max_length=100)
	range = models.IntegerField()

class Questions(models.Model):
	form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
	result_id = models.ForeignKey(Resultados, on_delete=models.CASCADE)
	eval = models.IntegerField()

class Login(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	permission = models.IntegerField()
	employee_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)