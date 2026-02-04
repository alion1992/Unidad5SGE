## Módulo VAR

El VAR (Video Assistant Referee) es un sistema de videoarbitraje utilizado en el fútbol para minimizar errores humanos del árbitro principal, revisando jugadas clave mediante cámaras de televisión en una sala técnica. Interviene únicamente en goles, penaltis, tarjetas rojas directas y errores de identidad. 

Desde la liga nos piden que hagamos un módulo para gestionar los partidos y calcular cuando vale utilizar el VAR en los partidos ya que cada intervención del VAR cuesta dinero en función de la revisión que se haga:

Revisar tarjeta roja: 1000 euros
Revisar agresión: 500 euros
Revisar fuera de juego: 300 euros
Revisar penalti: 200 euros

1) Desde nuestro módulo debemos poder gestionar Equipos a parte de conocer el nombre de los equipos es importante ver de que comunidad autónoma es: 

```python
  comunidad_autonoma = fields.Selection(
        selection=[
            ('andalucia', 'Andalucía'),
            ('aragon', 'Aragón'),
            ('castilla_la_mancha', 'Castilla-La Mancha'),
            ('madrid', 'Comunidad de Madrid'),
            ('valencia', 'Comunitat Valenciana'),
        ])
```
Es importante comprobar que no hay dos equipos con el mismo nombre por lo que si se da, debe informarse como error. Debe estar informado tambíen campos como la foto del escudo, año de fundación (Si tiene más de 100 años indicar que es equipo centenario) y nombre del estadio (no más de 50 caracteres).

2) El arbitro también debe poder gestinarse en nuestro módulo. A parte de ver su información completa de nombre y apellidos y la edad tenemos que registrar a que colegio arbitral pertenece ya que este dato es importante. Un arbitro nunca va a poder pitar a un equipo de su comunidad autónoma. El colegio arbitral tiene pocas peticiones pero nunca aceptan que un arbitro nuevo sea mayor de 40 años.

3) Gestión de los partidos. Esta es la parte más importante de nuestro módulo. Debemos tener los 2 equipos involucrados en el partido. El arbitro designado y las intervenciones del VAR con el total del dinero que ha costado el partido.
4)  Deben crearse tanto los formularios y vistas de búsquedas de forma funcional y la vista Kanban de los diferentes equipos agrupados por la comunidad autónoma que pertenecen.

Aclaraciones sobre el diseño: 
- Las opciones de menú por un lado Gestión: Incluye la gestión de Equipos y Árbitros y Partidos que lleva directamente a la pantalla de búsqueda de partidos.
- Agrupar los campos del formulario de partidos por un lado la zona de equipos y arbitro y por otro lado los datos del VAR.
  
- 


