# Python Moni Test

Se debe desarrollar sitio web en el que se registran pedido de prestamos de usuarios que acceden a el.
El usuario no necesita registrarse para solicitar un préstamo.
Para definir si al usuario se le aprueba o no el préstamoo usaremos una API definida debajo.

endpoint: http://scoringservice.moni.com.ar:7001/api/v1/scoring/
ejemplo: http://scoringservice.moni.com.ar:7001/api/v1/scoring/?document_number=30156149&gender=M&email=fran@mail.com
ACLARACION: usar esta api, no implementarla.

El formulario de pedido de prestamos el usuario debe ingresar dni, nombre y apellido, genero, email y monto solicitado. 
El usuario luego de ingresar los datos debe recibir la respuesta negativa o positiva en la misma página que ingreso sus datos.
Contemplar casos de datos ingresados con errores.

También se debe desarrollarse un sitio de administración en el que se puedan ver los pedidos de préstamo, con la opción de editarlos y eliminarlos. A este sitio solo pueden acceder usuarios administradores. No usar admin de Django.

### Installations

```sh
$  pip install -r requirements.txt
```
#### Migrations

```sh
$ python manage.py makemigrations
```
```sh
$ python manage.py migrate
```
```sh
$ python manage.py runserver
```

If you need to runserver in a specific port
```sh
$ python manage.py runserver localhost:9000
```
#### Create Super User
```sh
$ python manage.py createsuperuser

```

### CRUD
####List loans
<<server:port>>/loans/

####Create a new loan
<<server:port>>/loans/create/

####Update a loan
<<server:port>>/loans/update/<id>

####Delete a loan
<<server:port>>/loans/delete/<id>

####Loan Detail
<<server:port>>/loans/detail/<id>
