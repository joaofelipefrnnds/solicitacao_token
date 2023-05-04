from distutils.command.upload import upload
from django.db import models



class Cargo(models.Model):
    descricao=models.CharField(max_length=100)
    cadastrado_em=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descricao

class Coordenadoria(models.Model):
    descricao=models.CharField(max_length=100)
    cadastrado_em=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

class Departamento(models.Model):
    descricao=models.CharField(max_length=100)
    cadastrado_em=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    
class Servidor(models.Model):
    nome=models.CharField(max_length=100)
    cpf=models.CharField(max_length=11)
    rg=models.CharField(max_length=6)
    telefone=models.CharField(max_length=11)
    email=models.EmailField(max_length=256)
    anexo=models.FileField(upload_to="static/solicitante_imgs/", null=True)
    fk_cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE) # referencia como chave estrangeira a classe/tabela "MARCA"
    fk_coordenadoria=models.ForeignKey(Coordenadoria, on_delete=models.CASCADE) # referencia como chave estrangeira a classe/tabela "MARCA"
    fk_departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE) # referencia como chave estrangeira a classe/tabela "MARCA"
    status=models.BooleanField(default=True)
    cadastrado_em=models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.nome





    


