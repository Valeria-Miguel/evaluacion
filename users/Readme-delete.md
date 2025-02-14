# Título Eliminación de un usuario existente

permite eliminar  un usuario del sistema

## REQUERIMIENTOS

El usuario debe ser Administrador 

## OBSERVACIONES O CORRECCIONES

solo Admin puede eliminar una usuario
## URL

http://127.0.0.1:8000/api/users/users/{id}/

## MÉTODO HTTP 

DELETE 

## HEADERS

| HEADER               | VALOR                   | DESCRIPCIÓN |
| -------------------- | ----------------------- | ----------- |
| Authentication-token | TOKEN                 | Token de autenticación |

## PARÁMETROS  

| NOMBRE DEL PARÁMETRO | VALOR | DESCRIPCIÓN |
| -------------------- | ----- | ----------- |
|id                   |Integer	|ID del usuario 

## 

## RESPUESTA 

http://127.0.0.1:8000/api/users/users/9



​          
## EJEMPLO DE RESPUESTA
Respuesta de eliminacion exitosa:
```json
  {
   []
  }
```