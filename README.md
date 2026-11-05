# Tecnologías 

- Backend: Python / Django
- Frontend: HTML5, Tailwind CSS, JavaScript
- Base de datos: Sqlite

# Recursos

- https://www.monumentos.gob.cl/monumentos (Para información patrimonial)
- https://fontawesome.com/icons (Para íconos)
- https://tailwindflex.com/ (Para estilos)
- https://fonts.google.com/ (Para fuentes)


# Instalación 

## Prerrequisitos:
* `Python`
* `pip` 
* `git` 


Clonar el repositorio:
```powershell
git clone https://github.com/brojascc/CER2-ROJASBENJAMIN.git PatrimonioVivo
cd PatrimonioVivo
```

# Instalación de Dependencias

```powershell
pip install Django==5.2.18
```

# Configurar Base de datos

```powershell
python manage.py makemigrations
python manage.py migrate
```
## Poblar base de datos a partir de archivo CSV

```powershell
python manage.py importar_lugares lugares_patrimoniales.csv
```


Crear un superusuario para administrar la base de datos en admin.
```powershell
python manage.py createsuperuser
```


# Ejecutar la aplicación

```powershell
python manage.py runserver
```
Ingresa la dirección `http://127.0.0.1:8000/` en el navegador para acceder a la página.


