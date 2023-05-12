from source.screen import Window
from source import keyboard as kb


window = Window()
window.set_size((256, 256))
window.set_title("Кубойд")


while window.launched:
    for event in window.get_event():
        if event.type == kb.QUIT:
            window.close(lambda : quit())
    window.update()
    window.framerate_tick()
