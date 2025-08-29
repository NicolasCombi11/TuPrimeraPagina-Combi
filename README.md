
## Tu Primera Página

## Descripción del Proyecto
Este es un proyecto de blog desarrollado con **Python** y el framework **Django**. La idea detrás de "Tu Primera Página" es servir como una plataforma para que aspirantes a desarrolladores web puedan encontrar tutoriales, consejos y guías para construir su primer sitio web.

La aplicación cuenta con un sistema de administración robusto, perfiles de usuario, un sistema de autenticación completo y una app de mensajería para fomentar la comunicación entre los usuarios. Es un proyecto de aprendizaje que demuestra las funcionalidades principales de Django, desde la gestión de modelos hasta la implementación de un diseño moderno y responsivo.

## Características Principales

* **Sistema de Blog Completo**: Crea, edita y elimina posts de forma sencilla. Cada post puede incluir imágenes y texto enriquecido.
* **Autenticación de Usuarios**: Los usuarios pueden registrarse, iniciar sesión, cerrar sesión y gestionar sus perfiles, incluyendo la carga de avatares.
* **App de Mensajería**: Un sistema de mensajería interno que permite a los usuarios enviar y recibir mensajes directos.
* **Buscador Funcional**: Un buscador integrado para encontrar posts por título o contenido.
* **Diseño Profesional**: La interfaz ha sido diseñada para ser limpia, moderna y fácil de usar, inspirada en las mejores prácticas de diseño web.

## Cómo Instalar y Usar

1.  **Clonar el repositorio**:
    ```bash
    git clone [https://github.com/NicolasCombi11/TuPrimeraPagina-Combi.git](https://github.com/NicolasCombi11/TuPrimeraPagina-Combi.git)
    cd TuPrimeraPagina-Combi
    ```

2.  **Crear y activar un entorno virtual**:
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate
    ```

3.  **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar las migraciones**:
    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (para el panel de administración)**:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Iniciar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```
    El sitio estará disponible en `http://127.0.0.1:8000/`.

## Autor

Este proyecto fue desarrollado por **Nicolás Combi** como parte de un bootcamp del curso Python/Django.

---

