class ConsoleLogger:
    def __init__(self):
        self.text = ""

    def _format_text(self, to_write):
        output = ""
        assert 'command' in to_write, to_write
        command = to_write['command']
        category = ""
        quantity = ""
        if 'category' in to_write:
            category = to_write['category']
        if 'quantity' in to_write:
            quantity = to_write['quantity']
        output += "Command called: {} {} {}".format(command, category,
                                                    quantity)
        return output

    def add_text(self, text):
        formatted_text = self._format_text(text)
        self.text += formatted_text
        return True