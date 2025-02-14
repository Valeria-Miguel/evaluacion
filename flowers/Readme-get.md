# Título

Este endpoint permite obtener la lista de flores

## REQUERIMIENTOS

cualquier usuario puede ves la lista

## OBSERVACIONES O CORRECCIONES

Este endpoint debe retornar todos los registros de flores

## URL
http://127.0.0.1:8000/api/flowers/list

## MÉTODO HTTP 

GET

## HEADERS

| HEADER               | VALOR                 | DESCRIPCIÓN |
| -------------------- | --------------------- | ----------- |
| Authentication-token | TOKEN                 | token de autenticación |


## PARÁMETROS
| NOMBRE DEL PARÁMETRO     | VALOR | DESCRIPCIÓN |
| ------------------------ | ----- | ----------- |
|name	                     |String  |nombre de la flor
|price	                   |Float	  |precio de la flor
|stock	                   |Integer	|cantidad disponible
|description	             |String	|descripción opcional
|created_by	               |Integer  |	ID del empleado que crea la flor (admin o empleado)|
|created_at	               |DateTime |	fecha de creación de la flor|


## RESPUESTA 

```json
[
  {
    "id": 8,
    "name": "Rosa qqqqqq",
    "price": "150.50",
    "stock": 25,
    "description": "Una hermosa rosa sqqqqqqqqqqqqqqqqqqqq.",
    "created_at": "2025-02-13T23:47:34.444441Z",
    "created_by": null
  }
]
```


​      
## EJEMPLO DE RESPUESTA

```json
  [
  {
    "id": 8,
    "name": "Rosa china",
    "price": "150.50",
    "stock": 25,
    "description": "Una hermosa rosa .",
    "created_at": "2025-02-13T23:47:34.444441Z",
    "created_by": null
  }
]
```
o no estar autenticado 
```json
[
{
  "detail": "Authentication credentials were not provided."
}]
```