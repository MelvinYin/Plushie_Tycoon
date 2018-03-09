from defaults import starting_time

class TimeSteps:
    def __init__(self):
        self.time_steps = starting_time

    def update(self, time_steps):
        self.time_steps = time_steps
        return True

    def add(self, ):
