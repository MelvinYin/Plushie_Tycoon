from abc import ABC

class ActorBase(ABC):
    def __init__(self):
        self.base_p_ref = 13  # move to defaults