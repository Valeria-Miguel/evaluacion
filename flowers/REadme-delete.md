# Título Eliminación de una flor existente

permite eliminar una flor del sistema

## REQUERIMIENTOS

El usuario debe ser Administrador 

## OBSERVACIONES O CORRECCIONES

solo Admin puede eliminar una flor.
## URL

http://127.0.0.1:8000/api/flowers/delete/{id}/

## MÉTODO HTTP 

DELETE 

## HEADERS

| HEADER               | VALOR                   | DESCRIPCIÓN |
| -------------------- | ----------------------- | ----------- |
| Authentication-token | TOKEN                 | Token de autenticación |

## PARÁMETROS  

| NOMBRE DEL PARÁMETRO | VALOR | DESCRIPCIÓN |
| -------------------- | ----- | ----------- |
|id                   |Integer	|ID de la flor a eliminar

## 

## RESPUESTA 

http://127.0.0.1:8000/api/flowers/delete/8



​           

## EJEMPLO DE RESPUESTA

```json
  {
   []
  }
```