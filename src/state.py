from decimal import Decimal
from typing import Callable


class State:
    __energy: Decimal
    __energy_listeners: dict[int, Callable[[Decimal], None]]
    __energy_next_id: int

    def __init__(self):
        self.__energy = Decimal(0)
        self.__energy_listeners = {}
        self.__energy_next_id = 0

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value: Decimal):
        self.__energy = value

        for listener in self.__energy_listeners.values():
            listener(value)

    def register_energy_listener(self, listener: Callable[[Decimal], None]) -> int:
        listener_id = self.__energy_next_id
        self.__energy_next_id += 1
        self.__energy_listeners[listener_id] = listener
        return listener_id

    def unregister_energy_listener(self, listener_id: int):
        self.__energy_listeners.pop(listener_id)
