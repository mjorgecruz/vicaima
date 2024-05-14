from django.db import models

class Colaboradores(models.Model):
	colaborador_id = models.IntegerField()
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	function = models.CharField(max_length=100)
	admission_date = models.DateField()
	functional_group = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	
# class Correlacoes(models.Model):
# 	colaborador_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
# 	evaluator_id = models.ForeignKey(Colaboradores.colaborador_id, on_delete=models.CASCADE)
# 	director_id = models.ForeignKey(Colaboradores.colaborador_id, on_delete=models.CASCADE)

class Eventos(models.Model):
	event_id = models.IntegerField()
	creation_date = models.DateField()
	evaluator_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)

class Resultados(models.Model):
	result_id = models.IntegerField()
	result = models.IntegerField()
	classification = models.CharField(max_length=1)

class Avaliados(models.Model):
	avaliados_id = models.IntegerField()
	evaluation_id = models.ForeignKey(Eventos, on_delete=models.CASCADE)
	evaluated_id = models.ForeignKey(Colaboradores, on_delete=models.CASCADE)
	results_id = models.ForeignKey(Resultados, on_delete=models.CASCADE)
	comments = models.CharField(max_length=1000)



class Form(models.Model):
	form_id = models.IntegerField()
	form = models.CharField(max_length=100)
	range = models.IntegerField()

class Questions(models.Model):
	questions_id = models.IntegerField()
	form_id = models.ForeignKey(Form, on_delete=models.CASCADE)
	result_id = models.ForeignKey(Resultados, on_delete=models.CASCADE)
	eval = models.IntegerField()