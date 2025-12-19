# Sistema de Gestión de Usuarios y API (Evaluación Unidad 3)

Este proyecto corresponde al desarrollo de un sistema integral en Python, orientado a la gestión segura de usuarios locales y al consumo de una API REST pública (JSONPlaceholder).El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar), almacenando la información obtenida en una base de datos local SQLite, cumpliendo con los principios de la Programación Orientada a Objetos.Asignatura: Programación Orientada a Objetos (POOS)



##  Características
El sistema ha sido diseñado considerando requerimientos funcionales y no funcionales, destacando los siguientes aspectos:

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
