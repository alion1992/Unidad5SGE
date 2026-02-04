<h1>Implantación de módulos en Odoo</h1>

Para ello desde la terminal del docker de nuestro odoo ir a la carpeta donde tenemos configurados nuestros addons y lanzar

En la carpeta mnt/extra-addons

<img width="351" height="130" alt="image" src="https://github.com/user-attachments/assets/ea6b846a-b0bd-4536-8f43-93afc42b5fd2" />


```bash
odoo scaffold clientes
```

Con ello hemos creado un módulo nuevo y se nos ha tenido que crear la siguiente estructura de carpetas:

<img width="285" height="453" alt="image" src="https://github.com/user-attachments/assets/e54b8448-8109-474d-aad2-42fa7aac0904" />



### __manifest__.py

Archivo más importante del módulo.

Define:

Nombre del módulo
Autor
Descripción
Dependencias (depends)
Archivos que se deben cargar (data)
Si es instalable o no
Si aparece como aplicación

Es, literalmente, la ficha técnica del módulo.
Odoo lo lee para saber qué cargar y cómo hacerlo.


```python
{
    'name': "Clientes Renta",

    'summary': "Este módulo va a conseguir calcular el salario neto de una persona.",

    'description': """
Long description of module's purpose
    """,

    'author': "Francisco Alía",
    'website': "www.company.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
```

### models.py

Aquí van los modelos Python que definen:

Las tablas de base de datos
Los campos (Char, Integer, Many2one…)
La lógica de negocio
Los métodos
Las restricciones

Ejemplo:

```python
class Clientes(models.Model):
     _name = 'clientes.clientes'
     _description = 'clientes.clientes'

     nombre = fields.Char()
     apellido = fields.Char()
     descripcion = fields.Text()

class Puesto(models.Model):

    _name = 'clientes.puesto'
    _description = 'tipo puesto trabajo'

    descripcion = fields.Char()
```

### views

Contiene los archivos XML con:
Vistas tree (lista)
Vistas form
Vistas kanban
Acciones
Menús
Formularios
Wizards

Odoo no genera vistas automáticamente, así que todo lo que se ve en la interfaz va aquí.

La vista tipo List esta asociada a la vista de búsqueda y datos

```xml
    <record model="ir.ui.view" id="clientes.list">
      <field name="name">Clientes</field>
      <field name="model">clientes.clientes</field>
      <field name="arch" type="xml">
        <tree>
          <field name="nombre"/>
          <field name="apellido"/>
          <field name="descripcion"/>
        </tree>
      </field>
    </record>
```

<img width="1697" height="277" alt="image" src="https://github.com/user-attachments/assets/53752510-b07d-4464-9213-31a635395e9a" />

## Formularios

Los formularios para introducir resultados (se crea por defecto pero podemos editarlos)

```xml
<record model="ir.ui.view" id="clientes_form_view">
    <field name="name">clientes.form</field>
    <field name="model">clientes.clientes</field>
    <field name="arch" type="xml">
        <form string="Cliente">
            <sheet>
                <group>
                    <field name="nombre"/>
                    <field name="apellido"/>
                    <field name="descripcion"/>
                </group>
            </sheet>
        </form>
    </field>
    </record>
```

<img width="1553" height="334" alt="image" src="https://github.com/user-attachments/assets/4b2bf250-9fb7-4d71-819e-87ea3fcb8e0a" />

El menú de la parte superior se configura de la siguiente forma:

```xml
<menuitem name="Renta" id="clientes.menu_root"/>
```
Por un lado tenemos a la unidad padre

<img width="103" height="54" alt="image" src="https://github.com/user-attachments/assets/0c0cddd2-1f6c-4d1c-9689-c9507e4cd0ee" />

A través de ese id configuramos sus hijos:

```xml
<menuitem name="Clientes" id="clientes.menu_1" parent="clientes.menu_root"/>
<menuitem name="Tipo Puesto" id="clientes.menu_2" parent="clientes.menu_root"/>
```

Es imprescindible asociarle la acción a la que van configuradas definidas previamente:

```xml
<menuitem name="Lista de Clientes" id="clientes.menu_1_list" parent="clientes.menu_1"
              action="clientes.action_window"/>
<menuitem name="Lista de Puestos" id="clientes.menu_2_list" parent="clientes.menu_2"
              action="clientes.action_window_puesto"/>
```

<img width="280" height="46" alt="image" src="https://github.com/user-attachments/assets/17fb9d89-7730-4282-88c8-30fd6ff0efcc" />


Las acciones las definimos de la siguiente forma:

```xml
    <record model="ir.actions.act_window" id="clientes.action_window">
      <field name="name">Clientes</field>
      <field name="res_model">clientes.clientes</field>
      <field name="view_mode">tree,form</field>
    </record>

    <record model="ir.actions.act_window" id="clientes.action_window_puesto">
      <field name="name">Puesto</field>
      <field name="res_model">clientes.puesto</field>
      <field name="view_mode">tree,form</field>
    </record>
```

### security


Aquí se definen los permisos del módulo.

Incluye:

ir.model.access.csv → permisos básicos CRUD
Registros de seguridad (record rules)
Grupos de usuario

Sin este archivo, Odoo no dejará acceder al modelo aunque exista.

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_clientes_clientes,clientes.clientes,model_clientes_clientes,base.group_user,1,1,1,1
access_clientes_puesto,clientes.puesto,model_clientes_puesto,base.group_user,1,1,1,1
```

<h2>Instalación del módulo en el odoo</h2>

<img width="1693" height="376" alt="image" src="https://github.com/user-attachments/assets/5df5c822-a2fa-421d-ab4e-c07bbe6e6863" />

En el buscador de aplicaciones estamos desarrollando módulos no aplicaciones por lo que tenemos que eliminar el filtro de aplicaciones:

<img width="1331" height="426" alt="image" src="https://github.com/user-attachments/assets/737bfd6c-75d4-4662-88bf-4d6b52c05d5d" />
<br>
<img width="373" height="191" alt="image" src="https://github.com/user-attachments/assets/cefa51aa-e965-463b-901a-d9ca85cf7a1c" />
<br>
<img width="199" height="138" alt="image" src="https://github.com/user-attachments/assets/71fbcd3e-096f-4f17-a136-353e27036bed" />

## RELACIONES

Odoo ofrece 3 tipos principales de relaciones:

1. Many2one → muchos registros apuntan a uno

2. One2many → uno tiene muchos (inversa del Many2one)

3. Many2many → muchos a muchos

### Many2one

Por ejemplo: muchos clientes pertenecen a una ciudad:

```python
ciudad_id = fields.Many2one(
    'res.city',
    string='Ciudad'
)
```
<strong> ¿Qué hace? </strong>

- Crea una FK en la tabla actual
- EL usuario selecciona un registro desde un desplegable

```python
class Clientes(models.Model):
    _name = 'clientes.cliente'

    nombre = fields.Char()
    ciudad_id = fields.Many2one('res.country.state', string='Ciudad')
```

### One2Many

Relación uno → muchos.
Es la inversa de Many2one, NO crea columna en la tabla.
Se apoya en un Many2one.

```python
class Proyecto(models.Model):
    _name = 'proyecto.proyecto'
    
    nombre = fields.Char()
    tareas_ids = fields.One2many('proyecto.tarea', 'proyecto_id')

class Tarea(models.Model):
    _name = 'proyecto.tarea'
    
    nombre = fields.Char()
    proyecto_id = fields.Many2one('proyecto.proyecto')
```

### Many2Many

Relación muchos ↔ muchos.
Ejemplo: una tarea puede usar varias tecnologías y una tecnología puede estar en muchas tareas.

```python
tecnologia_ids = fields.Many2many('proyecto.tecnologia', string='Tecnologías')
```

- Crea automáticamente una tabla intermedia: proyecto_tarea_proyecto_tecnologia_rel
- Permite seleccionar múltiples valores desde un widget

```python
class Tarea(models.Model):
    _name = 'proyecto.tarea'

    nombre = fields.Char()
    tecnologia_ids = fields.Many2many('proyecto.tecnologia')

class Tecnologia(models.Model):
    _name = 'proyecto.tecnologia'

    nombre = fields.Char()
```
### Campos computados

Es un campo cuyo valor:

- Se calcula mediante un método Python

- Se actualiza automáticamente cuando cambian otros campos

- Puede guardarse en base de datos o no

```python
from odoo import models, fields, api

class Pedido(models.Model):
    _name = 'mi.pedido'

    precio = fields.Float()
    cantidad = fields.Integer()
    total = fields.Float(
        compute='_compute_total',
        store=True
    )

    @api.depends('precio', 'cantidad')
    def _compute_total(self):
        for record in self:
            record.total = record.precio * record.cantidad
```

Indica el método que calcula el valor.

```python
compute='_compute_total'
```

Declara de qué campos depende el cálculo.

```pythob
@api.depends('precio', 'cantidad')
```
## Vista Kanban

```xml
<!--Vista Kanban-->
    <record id="vista_kanban_persona" model="ir.ui.view">
    <field name="name">persona kanban</field>
    <field name="model">vuelta.persona</field>
    <field name="arch" type="xml">
        <kanban default_group_by="nombre">
            <field name="nombre"/>
            <field name="apellido1"/>
            <field name="apellido2"/>
             <templates>
                <t t-name="kanban-box">
                    <div class="oe_kanban_card">
                        <strong>
                            <field name="nombre"/>
                        </strong>
                        <div>
                            <field name="apellido1"/>
                        </div>
                        <div>
                            <field name="apellido2"/>
                        </div>
                    </div>
                </t>
            </templates>
        </kanban>
    </field>
    </record>
```

## Log

Odoo usa el sistema estándar de logging de Python.

```python
import logging

_logger = logging.getLogger(__name__)
```

### Escribir mensajes en el log

```python
_logger.info("Creando proveedor")
_logger.warning("Proveedor sin email")
_logger.error("Error al crear proveedor")
_logger.debug("Valores recibidos: %s", vals)
```

## Métodos del ORM

| Método        | Cuándo se ejecuta | Uso típico                   |
| ------------- | ----------------- | ---------------------------- |
| `create`      | Al crear          | Valores por defecto, códigos |
| `write`       | Al editar         | Control de cambios           |
| `unlink`      | Al borrar         | Prohibir borrado             |
| `search`      | Buscar            | Consultas                    |
| `browse`      | Por ID            | Acceso directo               |
| `filtered`    | En memoria        | Filtros rápidos              |
| `@depends`    | Automático        | Cálculos                     |
| `@constrains` | Validación        | Reglas                       |


En Odoo, los métodos create y write permiten interceptar la creación y modificación de registros para aplicar lógica de negocio, automatizaciones o validaciones.

### Método create

El método create() se ejecuta antes de que el registro se guarde en la base de datos.

Se usa principalmente para:

- Validar datos antes de crear el registro (este será nuestro caso)
- Generar valores automáticamente 
- Crear registros relacionados
- Normalizar datos

```python
@api.model
    def create(self, vals):
        if vals.get('edad', 0) < 0:
            raise ValidationError("La edad no puede ser negativa")

        return super().create(vals)
```

SIEMPRE llamar a super()
Si no lo haces, el registro no se guardará correctamente.

### Método write

Se ejecuta cuando se modifica un registro existente.

Usos habituales:

- Evitar cambios no permitidos
- Auditar modificaciones
- Recalcular datos
- Bloquear estados

```python
def write(self, vals):

    if 'edad' in vals and vals['edad'] < 0:
        raise ValidationError("La edad no puede ser negativa")

    return super().write(vals)
```
 RECORDAR: Si el campo no ha sido modificado no va el el vals por lo que tendremos que comprobar nulos antes.

### Validaciones con api constrains

Se ejecuta automáticamente cuando cambian los campos indicados.

```python


@api.constrains('edad')
def _check_edad(self):
    for record in self:
        if record.edad < 18:
            raise ValidationError("El alumno debe ser mayor de edad")
```
