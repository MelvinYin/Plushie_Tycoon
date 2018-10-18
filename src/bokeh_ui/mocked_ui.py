from global_config import Res, Prod
from widgets.mocked import mock_callbacks

class mock_UI:
    def __init__(self, initial_data, callback):
        self.check_input(initial_data)
        self.check_callback(callback)

    def check_input(self, initial_data, length=None):
        assert len(initial_data) == 2
        assert Res in list(initial_data.keys())
        assert Prod in list(initial_data.keys())
        for res in Res:
            assert res.name in list(initial_data[Res].keys())
        for prod in Prod:
            assert prod.name in list(initial_data[Prod].keys())
        assert 'time' in list(initial_data[Res].keys())
        assert 'time' in list(initial_data[Prod].keys())

        for category in (Res, Prod):
            for item in category:
                if not length:
                    length = len(initial_data[category][item.name])
                    continue
                assert length == len(initial_data[category][item.name])
        return True


    def check_callback(self, callback):
        for call in mock_callbacks:
            ret = callback(call)
            self.check_input(ret, length=1)
        return True


if __name__ == "__main__":
    from figures.mocked import mock_init, mock_update1, mock_update2, \
        mock_update3

    call_count = 0
    def callback(call):
        global call_count
        assert call in mock_callbacks
        if call_count == 0:
            call_count += 1
            return mock_update1
        elif call_count == 1:
            call_count += 1
            return mock_update2
        else:
            return mock_update3

    mock = mock_UI(mock_init, callback)
