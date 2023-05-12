from typing import Callable

from pygame.event import get as pg_get_event
from pygame.display import set_caption
from pygame.display import set_icon
from pygame.display import set_mode
from pygame import quit as pg_quit
from pygame.display import update
from pygame.event import Event
from pygame.time import Clock
from pygame import Surface


class Window:
    __clock = Clock()
    def __init__(self) -> None:
        self.launched: bool = False
        self.fps: int = 30
        self.surface: Surface
        self.width: int
        self.height: int

    def set_title(self, title: str) -> None:
        set_caption(title)

    def set_icon(self, icon: Surface) -> None:
        set_icon(icon)

    def set_size(self, size: tuple[int, int]) -> None:
        self.launched = True
        self.width, self.height = size
        self.surface = set_mode(size)

    def get_event(self) -> list[Event]:
        return pg_get_event()

    def framerate_tick(self) -> int:
        return self.__clock.tick(self.fps)

    def update(self) -> None:
        update()

    def close(self, end_function: Callable = lambda : False) -> None:
        pg_quit()
        end_function()
