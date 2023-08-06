## Como executar a aplicação
Execute os comandos abaixo:
1. ```python3 -m venv ./venv```
2. ```source venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```python api.py```

## Testando
```shell
curl http://127.0.0.1:5000/municipio-bairros?municipio=rio-de-janeiro
```
```json
{
    "municipio": "rio-de-janeiro",
    "bairros": [
        "Portuária",
        "Centro",
        "Rio Comprido",
        "Botafogo",
        "Copacabana",
        "Lagoa",
        "São Cristovão",
        "Tijuca",
        "Vila Isabel",
        "Ramos",
        "Penha",
        "Méier",
        "Irajá",
        "Madureira",
        "Jacarepaguá",
        "Bangu",
        "Campo Grande",
        "Santa Cruz",
        "Ilha do Governador",
        "Ilha de Paquetá",
        "Anchieta",
        "Santa Teresa",
        "Barra da Tijuca",
        "Pavuna",
        "Guaratiba",
        "Inhaúma",
        "Rocinha",
        "Jacarezinho",
        "Complexo do Alemão",
        "Maré",
        "Realengo",
        "Cidade de Deus",
        "Vigário Geral"
    ]
}
```
Seja feliz. :smile: