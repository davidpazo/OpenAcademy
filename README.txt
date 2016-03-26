Para comenzar con el modulo de Open Academy, nos conectamos desde putty al servidor de odoo.
Nos situamos en la carpeta de addons (opt/odoo/addons)y con el siguiente comando: 

----> odoo.py scaffold openacademy addons

Autogeneramos toda la estructura del modulo que vemos. 

Creamos un XML en la carpeta views, llamado openacademy.xml, que contendra el formulario y sus pestañas.

En el models.py añadimos la clase sessions, y su menu(formulario) correspondiente en el openacademy.xml

Y Relacionamos los campos entre el formulario de cursos y de sesiones escribiendo el correspondiente codigo en el openacademy.xml




