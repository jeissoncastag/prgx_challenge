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
