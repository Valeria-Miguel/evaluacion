# Título

Este endpoint permite obtener la lista de usuarios

## REQUERIMIENTOS

cualquier usuario puede ves la lista

## OBSERVACIONES O CORRECCIONES

Este endpoint debe retornar todos los registros de usuarios

## URL

http://127.0.0.1:8000/api/users/users/

## MÉTODO HTTP 

GET

## HEADERS

| HEADER               | VALOR                 | DESCRIPCIÓN |
| -------------------- | --------------------- | ----------- |
| Authentication-token | TOKEN                 | token de autenticación |


## PARÁMETROS
| NOMBRE DEL PARÁMETRO     | VALOR | DESCRIPCIÓN |
| ------------------------ | ----- | ----------- |
|id                       |Integer  |identificador del usuario
|username                 |String   |nombre de usuario
|email                    |String   |correo electrónico
|first_name               |String   |nombre del usuario
|last_name                |String   |primer apellido
|second_last_name         |String   |segundo apellido (opcional)

## RESPUESTA 

```json
[
  [
  {
    "id": 1,
    "username": "dulceMiguel",
    "email": "2022371092@uteq.edu.mx",
    "first_name": "",
    "last_name": "",
    "second_last_name": null
  },
  {
    "id": 2,
    "username": "florista123",
    "email": "florista@floreria.com",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
  },
  {
    "id": 3,
    "username": "dul",
    "email": "dul@gmail.com",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
  },
  {
    "id": 8,
    "username": "valess",
    "email": "valess@floreria.com",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
  },
  {
    "id": 9,
    "username": "ssss",
    "email": "ssss@floreria.com",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
  }
]
]
```


​      
## EJEMPLO DE RESPUESTA

```json
  [
    {
    "id": 9,
    "username": "ssss",
    "email": "ssss@floreria.com",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
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