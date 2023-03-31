# M5 - Kopa do Mundo

## Como rodar os testes localmente
 - Verifique se os pacotes pytest e/ou pytest-testdox estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o pytest e/ou pytest-testdox e/ou pytest-django em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest pytest-testdox -y
```
---

## Próximos passos:

### 1 Crie seu ambiente virtual:
```shell
python -m venv venv
```

### 2 Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

### 3 Instalar o pacote <strong>pytest-testdox</strong>:

```shell
pip install pytest-testdox pytest-django
```


### 4 Rodar os testes referentes a cada tarefa isoladamente:

Exemplo:

- Tarefa 0

```shell
pytest --testdox -vvs tests/tarefas/tarefa_0/
```

---

## Execução de testes a partir da tarefa 1
A partir de agora, para os testes das tarefas 1, 2 e 3, já que começaremos a usar o Django, precisaremos de um arquivo **pytest.ini**, você **DEVE** cria-lo na raiz do projeto, depois de criar esse aquivo você precisa adicionar nele a seguinte configuração:

```python
[pytest]
DJANGO_SETTINGS_MODULE = <kopa_do_mundo>.settings
```

**IMPORTANTE**:  Troque <nome_do_projeto> para o nome do pacote onde fica o arquivo settings.py do projeto Django.

- Tarefa 1


```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Tarefa 2

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```
- Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo: executar somente "test_can_get_product_by_id".

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_get_product_by_id.py::TestGetProductById::test_can_get_product_by_id
```
---

Os testes referentes as funcionalidades extras não são executados por padrão caso você não especifique o caminho até eles. Então caso você queira os executar, rode:

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/extra_add_product.py
```
