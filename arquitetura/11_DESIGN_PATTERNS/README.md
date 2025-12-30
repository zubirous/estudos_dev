# 11. DESIGN PATTERNS (Padrões de Projeto)

## Singleton
Garante apenas uma instância de uma classe.

```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## Factory
Cria objetos sem especificar a classe exata.

```python
class AnimalFactory:
    @staticmethod
    def criar(tipo):
        if tipo == "cachorro":
            return Cachorro()
        elif tipo == "gato":
            return Gato()
```

## Repository
Abstrai acesso a dados.

```python
class UsuarioRepository:
    def buscar_por_id(self, id):
        pass
    
    def salvar(self, usuario):
        pass
```

## Observer
Define dependência um-para-muitos entre objetos.

```python
class EventoManager:
    def __init__(self):
        self.observers = []
    
    def notificar(self, evento):
        for observer in self.observers:
            observer.atualizar(evento)
```

## Strategy
Define família de algoritmos intercambiáveis.

```python
class PagamentoProcessor:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def processar(self, valor):
        return self.estrategia.pagar(valor)
```
