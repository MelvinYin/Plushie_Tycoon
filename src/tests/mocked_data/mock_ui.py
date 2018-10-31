from .mock_widget import mock_callbacks

class mock_UI:
    def __init__(self, initial_data, callback, specs):
        self.run_callback(callback)

    def run_callback(self, callback):
        for call in mock_callbacks:
            callback(call)