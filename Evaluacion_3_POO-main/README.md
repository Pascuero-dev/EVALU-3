# Sistema de Gestión de Usuarios y API (Evaluación Unidad 3)

Este proyecto implementa un sistema completo en **Python** que gestiona usuarios locales con seguridad (hashing) y consume la API pública de **JSONPlaceholder** para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar), persistiendo los datos en una base de datos **SQLite**.


**Asignatura:** Programación Orientada a Objetos (POOS)

##  Características
El sistema cumple con los requerimientos funcionales y no funcionales:

* **Arquitectura en Capas:** Estructura modular (Negocio, Datos, Servicios, Modelos, Auxiliares).
* **Seguridad:** Encriptación de contraseñas utilizando `PBKDF2` con `SHA256` y `Salt`.
* **Base de Datos:** Persistencia local automática con **SQLite**.
* **Consumo de API:**
    * `GET`: Descarga posts y los guarda en base de datos local.
    * `POST`: Envía nuevos datos a la API.
    * `PUT`: Actualiza registros en la API.
    * `DELETE`: Elimina registros en la API.
* **Manejo de Errores:** Control de excepciones HTTP y de conexión.

##  Requisitos
* Python 3.12 o superior.
* No requiere instalación de librerías externas (`pip install` no es necesario), utiliza solo librerías estándar.

##  Estructura del Proyecto
```text
API_IEI_171_N2/
├── auxiliares/      # Seguridad y Hashing
├── datos/           # Conexión SQLite y creación de tablas
├── modelos/         # Clases POO (Usuario, Post)
├── negocio/         # Lógica principal del sistema
├── servicios/       # Comunicación HTTP con API externa
└── main.py          # Menú principal de ejecución