#  Registrar flores

Este endpoint permite registrar una nueva flor en el sistema

## REQUERIMIENTOS
El usuario debe estar autenticado
El usuario debe tener permisos de create para flores (Administrador o Empleado)

## OBSERVACIONES O CORRECCIONES

Asegurate de que el campo de precio, stock, decripcion y nombre sean obligatorios para crear la flor.

## URL

[URL del endpoint.](http://127.0.0.1:8000/api/flowers/create/)

## MÉTODO HTTP 

POST para este ejemplo

## HEADERS
| HEADER               | VALOR                 | DESCRIPCIÓN |
| -------------------- | --------------------- | ----------- |
| Authentication-token | TOKEN                 | Token de autenticación |


## PARÁMETROS  
| NOMBRE DEL PARÁMETRO     | VALOR | DESCRIPCIÓN |
| ------------------------ | ----- | ----------- |
|name	                     |String  |nombre de la flor
|price	                   |Float	  |precio de la flor
|stock	                   |Integer	|cantidad disponible
|description	             |String	|descripción opcional


## BODY
| CLAVE                           | TIPO   | DESCRIPCIÓN |
| ------------------------------- | ------ | ----------- |
|id	                              |Integer  |ID de la flor a modificar
|name	                            |String	  |nombre de la flor|
|price	                          |Real     |	precio de la flor|
|stock	                          |Integer  |	cantidad de flores disponibles|
|description	                    |String	  |descripción de la flor|
|created_by	                      |Integer  |	ID del empleado que crea la flor (admin o empleado)|
|created_at	                      |DateTime |	fecha de creación de la flor|



## RESPUESTA 

```json
{
  "name": "Rosa",
  "price": 12.99,
  "stock": 50,
  "description": "Rosa roja fresca"
}

```

​      
## EJEMPLO DE RESPUESTA

```json

{
  "id": 9,
  "name": "Rosa",
  "price": "12.99",
  "stock": 50,
  "description": "Rosa roja fresca",
  "created_at": "2025-02-14T04:28:24.794019Z",
  "created_by": null
}
```
cuando no agregamos los campos requeridos
## RESPUESTA 

```json
{
  "name": "Margarita",
  "description": "Flor amarilla y alegre"
}

```

​      
## EJEMPLO DE RESPUESTA

```json

{
  "name": [
    "This field is required."
  ],
  "price": [
    "This field is required."
  ],
  "stock": [
    "This field is required."
  ]
}
```