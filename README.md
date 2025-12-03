<h1>Implantación de módulos en Odoo</h1>

Para ello desde la terminal del docker de nuestro odoo ir a la carpeta donde tenemos configurados nuestros addons y lanzar

```bash
odoo scaffold clientes
```

Con ello hemos creado un módulo nuevo y se nos ha tenido que crear la siguiente estructura de carpetas:

```markdown
clientes/
 ├── controllers/
 ├── data/
 ├── models/
 ├── security/
 ├── views/
 ├── __init__.py
 ├── __manifest__.py
 └── ...
```
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
