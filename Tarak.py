from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random as r

app = Ursina()
Entity(model='plane', collider='box', scale=100, color=color.lime)
Sky(color=color.cyan)

p, s, t, o = FirstPersonController(), 0, 30, 0
st = Text(x=-.8, y=.4, scale=2)
tt = Text(x=.5, y=.4, scale=3, color=color.yellow) 

def spawn(): 
    Entity(model='cube', color=color.red, collider='box', x=r.uniform(-15,15), z=r.uniform(-15,15), y=2)

[spawn() for _ in range(12)]

def update():
    global t, o
    if not o:
        t -= time.dt
        tt.text, st.text = f'Time: {int(t)}', f'Score: {s}'
        if t <= 0: 
            o=1; Text('GAME OVER', scale=5, origin=(0,0), color=color.red); p.enabled=mouse.locked=0

def input(k):
    global s
    if k == 'left mouse down' and not o:
        h = raycast(camera.world_position, camera.forward)
        if h.hit and h.entity.color == color.red: 
            destroy(h.entity); s += 1; spawn()

app.run()