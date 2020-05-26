from bokeh.models.widgets import Button, Div
from bokeh.models.widgets.inputs import TextInput
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import row, column
from logs import log
import re
import os
import inspect
from bokeh.plotting import show, curdoc
from bokeh.models.layouts import WidgetBox, Spacer


class WarehouseTierSpecs:
    def __init__(self):
        self.name = 'WarehouseTier'
        self.title = "Console"
        self.text = '<p>'
        self.width = 50
        self.height = 20
        self.textbox_width = 400
        self.textbox_height = 500
        # Division by 2 so it fits well and within what bokeh uses.
        self.html_height = int(self.textbox_height / 2)

class WarehouseTierConsole:
    def __init__(self, specs):
        self.name = specs.name
        self.specs = specs
        self._paragraph = self._build_paragraph()
        self.figure = self._set_textbox(specs)

    def _build_paragraph(self):
        _style = dict()
        _style['height'] = '{}px'.format(self.specs.html_height)
        text = self._build_text(self.specs.tier, self.specs.cost)
        paragraph = Div(width=self.specs.textbox_width,
                        height=self.specs.textbox_height,
                        text=self.specs.text, style=_style)
        return paragraph

    def _set_textbox(self, specs):
        fig = column(row(Spacer(height=specs.height)),
                     row(Spacer(width=specs.width), self._paragraph))
        return fig

    def _build_text(self, current_tier, cost_to_upgrade):
        text = f'Current tier: {current_tier}<br />' \
            f'Cost to upgrade: {cost_to_upgrade}'
        return text

    def figure_update(self, add_line):
        # Can't get bokeh div to scroll to end, it'll always reset to top
        # even if scrollHeight==scrollTop, etc. Keep it like this for now.
        self._paragraph.text = self._build_text(add_line['tier'],
                                                add_line['cost'])
        return True

x = WarehouseTierConsole(WarehouseTierSpecs())
x.figure_update(dict(tier=1, cost=10000))
show(x.figure)