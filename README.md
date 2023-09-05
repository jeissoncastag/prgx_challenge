# Desafío de Entrevista para Llevar a Casa
Tenemos 2 tablas básicas: usuario y dirección. Utiliza el framework FastAPI y crea servicios REST para permitir la administración de usuarios.

## Requisitos de la API REST:
1. Crear usuarios con parámetros de entrada: usuario (id, nombre, apellido, correo electrónico y contraseña), y direcciones (id, dirección_1, dirección_2, ciudad, estado, código postal, país).
2. Recuperar usuarios por país.

Para la comunicación entre servicios, se pueden utilizar llamadas REST o gRPC para: Obtener información de usuario / Código de prueba de cliente de ejemplo.

## Configuración del Proyecto
A continuación se muestra una guía básica para configurar y ejecutar el proyecto:

### Instalación
1. Clona el repositorio.
`git clone https://github.com/tu-usuario/nombre-del-proyecto.git`

2. Ve al directorio del proyecto.
`cd nombre-del-proyecto`

3. Instala las dependencias.
`pip install -r requirements.txt`

### Ejecución
1. Inicia el servidor FastAPI.
`uvicorn main:app --reload`

### Uso
- Para crear un usuario, realiza una solicitud POST a `/api/users` con los datos del usuario en el cuerpo de la solicitud en formato JSON. El siguiente es un ejemplo:

```
{
    "id": 5,
    "first_name": "Lorena",
    "last_name": "Lopez",
    "mail": "lorelo@example.com",
    "password": "password123",
    "addresses": [
        {
            "id": 5,
            "address_1": "123 St 456",
            "address_2": "Apt 12",
            "city": "Tampa",
            "state": "Florida",
            "zip": "033101",
            "country": "USA"
        }
    ]
}
```

- Para recuperar usuarios por país, realiza una solicitud GET a `/api/users/{country}`.

**Paso 1: Ejecuta tu aplicación FastAPI**
Antes de probar tu aplicación con Postman, asegúrate de que tu aplicación FastAPI esté en funcionamiento. Para ejecutarla, abre una terminal, navega al directorio raíz de tu proyecto y ejecuta el siguiente comando (asegúrate de que las dependencias estén instaladas y el servidor esté en funcionamiento):

```bash
uvicorn main:app --reload
```

Esto iniciará tu aplicación en `http://127.0.0.1:8000`.

**Paso 2: Abre Postman**
Abre la aplicación Postman en tu sistema. Si aún no tienes Postman instalado, puedes descargarlo e instalarlo desde [https://www.postman.com/](https://www.postman.com/).

**Paso 3: Crea una nueva solicitud en Postman**
- En Postman, crea una nueva solicitud haciendo clic en "New" en la esquina superior izquierda y selecciona "Request".

**Paso 4: Configura la solicitud**
- Asigna un nombre descriptivo a la solicitud en el campo "Request Name".
- Selecciona el método HTTP adecuado (GET, POST) en el menú desplegable "HTTP Method".
- En la barra de URL, ingresa la URL completa de la ruta que deseas probar en tu aplicación FastAPI. Por ejemplo, si quieres probar la ruta `/users`, ingresa `http://127.0.0.1:8000/users`.

**Paso 5: Agrega parámetros y datos (si es necesario)**
- Si tu solicitud requiere parámetros o datos en el cuerpo de la solicitud, puedes configurarlos en las pestañas correspondientes en la parte inferior de la ventana de Postman.

**Paso 6: Envía la solicitud**
- Haz clic en el botón "Send" (Enviar) para enviar la solicitud a tu aplicación FastAPI.

**Paso 7: Observa la respuesta**
- En la parte inferior de la ventana de Postman, verás la respuesta de tu aplicación FastAPI. Esto incluirá el código de estado HTTP, la respuesta JSON u otros datos relevantes.

**Paso 8: Analiza la respuesta**
- Examina la respuesta para asegurarte de que tu API esté funcionando correctamente y que los datos sean los esperados.
