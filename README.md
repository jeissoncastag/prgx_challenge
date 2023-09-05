# Desafío de Entrevista para Llevar a Casa

Tenemos 2 tablas básicas: usuario y dirección. Utiliza el framework FastAPI y crea servicios REST para permitir la administración de usuarios. Eres libre de usar cualquier tipo de dato adecuado.

## Requisitos de la API REST:

1. Crear usuarios con parámetros de entrada: usuario (id, nombre, apellido, correo electrónico y contraseña), y direcciones (id, dirección_1, dirección_2, ciudad, estado, código postal, país).
2. Recuperar usuarios por país.

Para la comunicación entre servicios, se pueden utilizar llamadas REST o gRPC para:

- Obtener información de usuario.
- Código de prueba de cliente de ejemplo.

## Configuración del Proyecto

A continuación se muestra una guía básica para configurar y ejecutar el proyecto:

### Instalación

1. Clona el repositorio.

git clone https://github.com/tu-usuario/nombre-del-proyecto.git


2. Ve al directorio del proyecto.

cd nombre-del-proyecto

3. Instala las dependencias.

pip install -r requirements.txt


### Ejecución

1. Inicia el servidor FastAPI.

uvicorn main:app --reload


### Uso

- Para crear un usuario, realiza una solicitud POST a `/api/users` con los datos del usuario en el cuerpo de la solicitud en formato JSON.

- Para recuperar usuarios por país, realiza una solicitud GET a `/api/users/{country}`.

### Comunicación entre Servicios

Para comunicarse con otros servicios, puedes usar llamadas REST o gRPC. Aquí tienes un ejemplo de cómo obtener información de usuario utilizando REST:

```python
import requests

url = 'http://ruta-del-servicio/api/user-info/{user_id}'
response = requests.get(url)
data = response.json()
print(data)

Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Abre una solicitud de extracción en GitHub.
Licencia
Este proyecto está bajo la Licencia [nombre_de_la_licencia]. Consulta el archivo LICENSE.md para obtener más detalles.

Contacto
Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto con nosotros en [correo electrónico] o a través de Twitter.


Recuerda reemplazar `nombre-del-proyecto`, `tu-usuario`, `ruta-del-servicio`, y otros marcadores de posición con información específica de tu proyecto. También, asegúrate de proporcionar detalles adicionales sobre la licencia utilizada y la estructura real de tu proyecto si es necesario.


# Take-Home Interview Challenge

Para probar la aplicación FastAPI con Postman, sigue estos pasos:

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

- Selecciona el método HTTP adecuado (GET, POST, PUT, etc.) en el menú desplegable "HTTP Method".

- En la barra de URL, ingresa la URL completa de la ruta que deseas probar en tu aplicación FastAPI. Por ejemplo, si quieres probar la ruta `/users`, ingresa `http://127.0.0.1:8000/users`.

**Paso 5: Agrega parámetros y datos (si es necesario)**

- Si tu solicitud requiere parámetros o datos en el cuerpo de la solicitud, puedes configurarlos en las pestañas correspondientes en la parte inferior de la ventana de Postman.

**Paso 6: Envía la solicitud**

- Haz clic en el botón "Send" (Enviar) para enviar la solicitud a tu aplicación FastAPI.

**Paso 7: Observa la respuesta**

- En la parte inferior de la ventana de Postman, verás la respuesta de tu aplicación FastAPI. Esto incluirá el código de estado HTTP, la respuesta JSON u otros datos relevantes.

**Paso 8: Analiza la respuesta**

- Examina la respuesta para asegurarte de que tu API esté funcionando correctamente y que los datos sean los esperados.

Eso es todo. Has utilizado Postman para enviar solicitudes a tu aplicación FastAPI y recibir respuestas. Puedes repetir estos pasos para probar diferentes rutas y métodos de tu API según sea necesario. Asegúrate de que tu API esté funcionando y configurada correctamente antes de probarla con Postman.
