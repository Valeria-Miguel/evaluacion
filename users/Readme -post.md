#  Registrar ususarios

Endpoint para el registro de un nuevo usuario.
Este endpoint permite registrar un nuevo usuario en la aplicación, proporcionando los datos : nombre, apellido, email, etc. Al registrarse, se asignará automáticamente un rol de usuario básico.

## REQUERIMIENTOS
El usuario debe estar autenticado
El usuario debe tener permisos de registrar (Administrador o Empleado)
Django REST Framework configurado correctamente.

## OBSERVACIONES O CORRECCIONES

El cuerpo de la solicitud debe incluir los datos obligatorios como nombre, correo y contraseña(username, email, password.)
## URL

http://127.0.0.1:8000/api/users/register/

## MÉTODO HTTP 

El método es POST porque se enviarán datos del usuario que deben ser creados en la base de datos.

## HEADERS
| HEADER               | VALOR                   | DESCRIPCIÓN |
| -------------------- | ----------------------- | ----------- |
| Authentication-token | TOKEN                 | Token de autenticación |


## PARÁMETROS  
| NOMBRE DEL PARÁMETRO     | VALOR | DESCRIPCIÓN |
| ------------------------ | ----- | ----------- |
|username	                |string	  |nombre de usuario unico
|email	                    |string	  |correo electronico del usuario
|password	                |string	  |contraseña del usuario
|first_name	              |string	  |primer nombre del usuario
|last_name	                |string	  |apellido del usuario
|second_last_name	        |string	  |segundo apellido del usuario (opcional)


BODY


## BODY
| CLAVE                           | TIPO   | DESCRIPCIÓN |
| ------------------------------- | ------ | ----------- |
|username	                        |string	|nombre de usuario
|email	                          |string	|correo electronico
|password	                        |string	|contraseña
|first_name	                      |string	|primer nombre del usuario
|last_name	                      |string	|apellido del usuario
|second_last_name	                |string	|segundo apellido (opcional)


## RESPUESTA 

## RESPUESTA 

```json

{
    "username": "florista345",
    "email": "florista345@floreria.com",
    "password": "secreta123",
    "first_name": "Dul",
    "last_name": "Miguel",
    "second_last_name": "juan"
}



```


​      
## EJEMPLO DE RESPUESTA

```json

{
  "username": "florista345",
  "email": "florista345@floreria.com",
  "first_name": "Dul",
  "last_name": "Miguel",
  "second_last_name": "juan",
  "role": "Viewer"
}
```
