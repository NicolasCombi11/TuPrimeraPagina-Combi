
# TuPrimeraPagina-Combi

Proyecto Django estilo blog con patrón MVT. Incluye:

- Herencia de plantillas (`base.html` -> vistas)
- 3 modelos: `Author`, `Category`, `Post`
- Formularios para insertar datos en cada modelo
- Formulario de búsqueda sobre `Post`
- Admin habilitado
- README con guía paso a paso y orden para probar

## Estructura

```
TuPrimeraPagina-Combi/
├── TuPrimeraPaginaCombi/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── blog/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── author_form.html
│   ├── category_form.html
│   ├── post_form.html
│   ├── post_list.html
│   └── search.html
├── manage.py
├── requirements.txt
└── .gitignore
```

## Cómo correrlo localmente

> Requisitos: Python 3.10+

1. **Crear y activar entorno virtual** (sugerido)

```bash
python -m venv .venv
# Windows
. .venv/Scripts/activate
# Linux/Mac
. .venv/bin/activate
```

2. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

3. **Migraciones y superusuario**

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. **Levantar el servidor**

```bash
python manage.py runserver
```

5. **Probar en este orden**

- Ir a `/admin/` y/o usar los formularios públicos:
  - `/blog/autores/nuevo/` → crear al menos un Autor
  - `/blog/categorias/nueva/` → crear una Categoría
  - `/blog/posts/nuevo/` → crear un Post (elige Autor/Categoría)
  - `/blog/posts/` → ver listado
  - `/blog/buscar/?q=<palabra>` → buscar por título o contenido

> La página de inicio `/` lista accesos rápidos a todo lo anterior.

## Guía solicitada (paso a paso)

- Crear carpeta del proyecto y abrir en VSCode
- Crear `.gitignore` (incluido)
- Crear entorno virtual y **agregar su carpeta al `.gitignore`** (ya configurado)
- Inicializar git, primer commit, conectar a GitHub y hacer `push`
- Activar entorno virtual
- Instalar Django con `pip install Django` o `pip install -r requirements.txt`
- Crear `requirements.txt` con `pip freeze > requirements.txt` cada vez que instales paquetes
- **El proyecto y la app ya están creados:** `TuPrimeraPaginaCombi` y `blog`
- Probar con `python manage.py migrate` y `python manage.py runserver`
- Agregar la app a `INSTALLED_APPS` (**ya está**)
- `urls.py` en app y en proyecto (**ya están**), con `include()` (**hecho**)
- `TEMPLATES['DIRS']` configurado a `BASE_DIR / 'templates'` (**hecho**)
- Crear superusuario (**hazlo localmente**)
- Crear vistas, paths y templates (**hecho**)
- Crear modelos, migraciones y registrar en admin (**hecho, pero corre migraciones**)
- Crear formularios (`forms.Form`) y usarlos en vistas (**hecho**)

## Notas

- Base de datos: SQLite por defecto.
- Idioma: `es-ar`, Zona: `America/Argentina/Buenos_Aires`.
- Seguridad: `DEBUG=True`, solo para desarrollo.
- Para deploy, recuerda configurar `ALLOWED_HOSTS`, `STATIC_ROOT`, etc.

¡Éxitos con la entrega! ✨
