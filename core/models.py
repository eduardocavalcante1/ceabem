from django.db import models


class Pessoa(models.Model):
    cpf = models.CharField(max_length=11, null=False, blank=False)
    nome = models.CharField(max_length=60, null=False, blank=False)
    nomereduzido = models.CharField(max_length=20, null=False, blank=False)
    data_nascimento = models.DateField(auto_now=False, null=False, blank=False)
    endereco = models.CharField(max_length=60, null=False, blank=False)
    bairro = models.CharField(max_length=60, null=False, blank=False)
    complemento = models.CharField(max_length=45)
    cidade = models.CharField(max_length=60, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    telefone1 = models.CharField(max_length=11, null=False, blank=False)
    telefone2 = models.CharField(max_length=11)
    email = models.CharField(max_length=50, null=False, blank=False)
    estado_civil = models.CharField(max_length=45, null=False, blank=False)
    genero = models.CharField(max_length=45, null=False, blank=False)
    ativo = models.CharField(max_length=1, null=False, blank=False)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)

    def __str__(self):
        return self.cpf + '-' + self.nome


class Vinculo(models.Model):
    descricao = models.CharField(max_length=60, null=False, blank=False)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)


class Pessoa_Vinculo(models.Model):
    pessoa = models.ForeignKey(
        'Pessoa', related_name='pessoa_vinculo', on_delete=models.CASCADE)
    vinculo = models.ForeignKey(
        'Vinculo', related_name='vinculo_pessoa', on_delete=models.CASCADE)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)


class Atividade(models.Model):
    descricao = models.CharField(max_length=60, null=False, blank=False)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)


class Pessoa_Atividade(models.Model):
    pessoa = models.ForeignKey(
        'Pessoa', related_name='pessoa_atividade', on_delete=models.CASCADE)
    atividade = models.ForeignKey(
        'Atividade', related_name='atividade_pessoa', on_delete=models.CASCADE)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)


class Terapeuta(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    usuario_cadastro = models.IntegerField(null=False, blank=False)
    data_cadastro = models.DateTimeField(null=False, blank=False)
    usuario_alteracao = models.IntegerField(null=False, blank=False)
    data_alteracao = models.DateTimeField(null=False, blank=False)
    cancelado = models.CharField(max_length=1, null=False, blank=False)
