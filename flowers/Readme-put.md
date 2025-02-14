# Título  Modificación de los detalles de una flor

Permite modificar los detalles de una flor ya existente.

## REQUERIMIENTOS

el usuario debe ser Admin o Empleadoes

## OBSERVACIONES O CORRECCIONES

solo Admin o Empleado pueden modificar las flores.

## URL

http://127.0.0.1:8000/api/flowers/update/{id}/


## MÉTODO HTTP 

PUT para este ejemplo

## HEADERS

| HEADER       | VALOR                                    | DESCRIPCIÓN |
| ------------ | ---------------------------------------- | ----------- |
| Authentication-token | TOKEN                 | token de autenticación |

## PARÁMETROS

| NOMBRE DEL PARÁMETRO | VALOR                     | DESCRIPCIÓN |
| -------------------- | ------------------------- | ----------- |
|id	                    |Integer	                |ID de la flor a modificar

## BODY

| CLAVE                 | TIPO    | DESCRIPCIÓN |
| --------------------- | ------- | ----------- |
|id	                    |Integer    |ID de la flor a modificar
|name	                |String     |nombre de la flor
|price	                |Float	    |precio de la flor
|stock	                |Integer	|cantidad disponible
|description	        |String	    |descripción opcional
|created_by	            |Integer  |	ID del empleado que crea la flor (admin o empleado)|
|created_at	            |DateTime |	fecha de creación de la flor|


## RESPUESTA 

http://127.0.0.1:8000/api/flowers/update/9
```json
{
  "name": "Margarita Rosa",
  "price": 8.99,
  "stock": 120,
  "description": "Flor rosa de la variedad Margarita"
}

```


## EJEMPLO DE RESPUESTA
```json
  {
  "id": 9,
  "name": "Margarita Rosa",
  "price": "8.99",
  "stock": 120,
  "description": "Flor rosa de la variedad Margarita",
  "created_at": "2025-02-14T04:28:24.794019Z",
  "created_by": null
}
```