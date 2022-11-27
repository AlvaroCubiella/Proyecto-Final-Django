# Proyecto final para Coderhouse (Django - Python)

# Desarrollado por Cubiella, Alvaro

# Proyecto Final Framework Django 4.1 & Python 3.9

El objetivo es crear publicaciones de viajes e informes de datos ambientales de Oceanografía (Física, Química y Biológica).

El administrador puede:
- Crear posteo
- Administrar usuarios (permisos y grupos de trabajo)

El usuario registrado tiene acceso a:
- Ver los informes de la pagina
- Realizar busquedas de articulos viejos
- Publicar nuevos informes
- Editar/eliminar informes antiguos (segun permisos asignados por el Administrador)

El usuario final tiene acceso a:
- Ver los informes de la pagina
- Realizar busquedas de articulos viejos
- Registrarse

## Instalaciones desde Visual Studio Code

- Instalar Python

```bash
$ pip install python
```
- Instalar Django
```bash
$ pip install django
```
- Instalar Pilow
```bash
$ pip install pillow 
```
- Instalar ckeditor
```bash
$ pip install django-ckeditor
```
## Comprobando que todo funcione de manera correcta y que las versiones sean las correspondientes.

- Python en el PowerShell
```bash
$ python --version
Python 3.9.7
```
- Django en el shell
```ps
>>> import django
>>> django.VERSION
(4, 1, 2, 'final', 0)
>>>
```

## Lo primero que debemos hacer es crear nuestro repositorio en github  https://github.com/MartinMadda/Final-Coderhouse.git.

## Luego en VScode vamos a crear una nueva carpeta y vamos a abrir la terminal para clonar nuestro repositorio y asi poder trabajar en él de la siguiente manera:

```ps
git clone https://github.com/MartinMadda/Final-Coderhouse.git .
```
```ps
"Es muy importante el espacio y el .(punto) ya que asi nuestro repositorio no creara otras carpetas dentro de la nuestra."
```

```