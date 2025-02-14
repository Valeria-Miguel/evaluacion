# Título  Modificación de los detalles del usuario

Este endpoint permite modificar los detalles de un usuario ya existente.
## REQUERIMIENTOS

el usuario debe ser Admin o Empleadoes

## OBSERVACIONES O CORRECCIONES

solo Admin o Empleado pueden modificar los usuarios

## URL

http://127.0.0.1:8000/api/users/users/{id}/


## MÉTODO HTTP 

PUT 

## HEADERS

| HEADER       | VALOR                                    | DESCRIPCIÓN |
| ------------ | ---------------------------------------- | ----------- |
| Authentication-token | TOKEN                 | token de autenticación |

## PARÁMETROS

| NOMBRE DEL PARÁMETRO | VALOR                     | DESCRIPCIÓN |
| -------------------- | ------------------------- | ----------- |
|id	                    |Integer	                |ID del usuario

## BODY

| CLAVE                 | TIPO    | DESCRIPCIÓN |
| --------------------- | ------- | ----------- |
|id                     |Integer  |ID del usuario a modificar
|name                   |String   |nombre del usuario
|email                  |String   |correo electronico del usuario
|role                   |String   |Rol del usuario (views o Empleado)

## RESPUESTA 

http://127.0.0.1:8000/api/users/users/9
```json
{
    "username": "modificado",
    "email": "modificado@floreria.com",
    "first_name": "Dul",
    "last_name": "Miguel"
}

```


## EJEMPLO DE RESPUESTA
```json
{
  "id": 9,
  "username": "modificado",
  "email": "modificado@floreria.com",
  "first_name": "Dul",
  "last_name": "Miguel",
  "second_last_name": "juan"
}
```