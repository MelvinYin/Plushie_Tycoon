class UIInterface:
    # singleton
    def __init__(self, ge_update_func, ui_update_func):
        self.ge_update_func = ge_update_func
        self.ui_update_func = ui_update_func

    def widget_callback(self, label, *args):
        to_add = self.ge_update_func(label, *args)
        self.ui_update_func(to_add)
        return True

