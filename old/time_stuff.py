from defaults import starting_time






class TimeSteps:
    def __init__(self):
        self._time_steps = starting_time

    def __eq__(self, other):
        return self._time_steps == other

    def __add__(self, other):
        item = self._time_steps + other
        return item

    def __iadd__(self, other):
        self._time_steps += other
        return self

    def test_func(self):
        return True

    def __sub__(self, other):
        item = self._time_steps - other
        return item

    def __isub__(self, other):
        self._time_steps -= other
        return self