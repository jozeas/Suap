from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} {self.site} {self.tel}'

class Area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Periodo(models.Model):
    situacao = models.CharField(max_length=15)

    def __str__(self):
        return self.situacao
    
class Turma(models.Model):
    nome = models.CharField(max_length=40)
    periodo = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nome} {self.periodo}'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} {self.uf}'

class Tipo_avaliacao(models.Model):
    tipo = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    pai = models.CharField(max_length=40)
    mae = models.CharField(max_length=40)
    cpf = models.CharField(max_length=20)
    nascimento = models.DateField()
    email = models.CharField(max_length=40)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.pai} {self.mae} {self.cpf} {self.nascimento} {self.email} {self.cidade}'
    
class Curso(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.duracao_meses} {self.area} {self.instituicao}'
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.area}'
    
class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    

    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.data_inicio} {self.data_termino}'

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=150)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'  
    
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    num_faltas = models.PositiveIntegerField()

    

    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.num_faltas}'  
    
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=150)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    

    def __str__(self):
        return f'{self.descricao} {self.data} {self.curso} {self.disciplina} {self.pessoa}'  
    
class Disciplina_por_Curso(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.curso} {self.periodo}'