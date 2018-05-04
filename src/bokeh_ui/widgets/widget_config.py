from collections import namedtuple
from enum import Enum, auto, unique

# TO USE:
# from widget_config import transaction_specs, button_specs, set_specs

##############################################################################
# Global

from global_config import Res, Prod, Func

##############################################################################
# Internal

@unique
class WidgetNames(Enum):
    Transaction = auto()
    Action = auto()

##############################################################################
# Widget Attributes

class TransactionWidgetSpecs:
    def __init__(self):
        self.name = WidgetNames.Transaction
        self.width = 350
        self.height = 0
        self.header = self.set_header()
        self.RBG1 = self.set_RBG1()
        self.RBG2 = self.set_RBG2()
        self.RBG3 = self.set_RBG3()
        self.TI = self.set_TI()
        self.button = self.set_button()
        self.layout = self.set_layout()

    def set_header(self):
        Header = namedtuple("Header", 'width height title')
        header = Header(width=0,  # Text box
                        height=0,
                        title='TITLE123')
        return header

    def set_RBG1(self):
        labelmap = dict()
        labelmap[Func.buy] = "Func 1"
        labelmap[Func.sell] = "Func 2"
        labelmap[Func.make] = "Func 3"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Func.buy, Func.sell, Func.make],
                   labelmap = labelmap)
        return RBG

    def set_RBG2(self):
        labelmap = dict()
        labelmap[Res] = "Cat 1"
        labelmap[Prod] = "Cat 2"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Res, Prod],
                   labelmap = labelmap)
        return RBG

    def set_RBG3(self):
        labelmap = dict()
        labelmap[Res.cloth] = "Prod 1"
        labelmap[Res.stuff] = "Prod 2"
        labelmap[Res.accessory] = "Prod 3"
        labelmap[Res.packaging] = "Prod 4"
        labelmap[Prod.aisha] = "Prod 5"
        labelmap[Prod.beta] = "Prod 6"
        labelmap[Prod.chama] = "Prod 7"
        # noinspection PyTypeChecker
        assert len(labelmap) == len(Res) + len(Prod)
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=list(Res),
                   labelmap=labelmap)
        return RBG

    def set_TI(self):
        TI_ = namedtuple("Header", 'width height placeholder')
        TI = TI_(width=1,  # Text box
                 height=1,
                 placeholder='PLACEHOLDER123')
        return TI

    def set_button(self):
        Button = namedtuple("Header", 'width height label')
        button = Button(width=50,  # Size of button
                        height=0,
                        label="button123")
        return button

    def set_layout(self):
        Row_Specs = namedtuple("Row_Specs",
            field_names=['height', 'width', 'spacers'])

        header = Row_Specs(height=30,
                         width=100,  # Determine how close RBG is
                         spacers=[0])

        rbg1 = Row_Specs(height=40,
                         width=50,  # Determine when break between rows happen
                         spacers=[0])

        rbg2 = Row_Specs(height=40,
                         width=20,  # Determine how close RBG is
                         spacers=[0])

        rbg3 = Row_Specs(height=30,
                         width=0,  # Determine how close RBG is
                         spacers=[0])

        ti = Row_Specs(height=17,  # Spacing between widget cols
                         width=10,  # Spacing between widgets in same row.
                         spacers=[0])

        button = Row_Specs(height=0,  # Spacing between widget cols
                         width=200,  # Spacing between widgets in same row.
                         spacers=[0])

        layout = [header, rbg1, rbg2, rbg3, ti, button]
        return layout


class ButtonWidgetSpecs:
    def __init__(self):
        self.name = WidgetNames.Action
        self.width = 0
        self.height = 0
        self.header = self.set_header()
        self.RBG = self.set_RBG()
        self.button = self.set_button()
        self.layout = self.set_layout()

    def set_header(self):
        Header = namedtuple("Header", 'width height title')
        header = Header(width=0,  # Text box
                        height=0,
                        title='TITLE123')
        return header

    def set_RBG(self):
        labelmap = dict()
        labelmap[Func.next] = "Func 1"
        labelmap[Func.save] = "Func 2"
        labelmap[Func.load] = "Func 3"
        labelmap[Func.quit] = "Func 4"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=250,
                   height=17,
                   labels=[Func.next, Func.save, Func.load, Func.quit],
                   labelmap=labelmap)
        return RBG

    def set_button(self):
        Button = namedtuple("Header", 'width height label')
        button = Button(width=0,  # Size of button
                        height=0,
                        label="button123")
        return button

    def set_layout(self):
        Row_Specs = namedtuple("Row_Specs",
            field_names=['height', 'width', 'spacers'])

        row0 = Row_Specs(height=30,
                         width=100,  # Determine how close RBG is
                         spacers=[0])

        row1 = Row_Specs(height=40,
                         width=0,  # Determine when break between rows happen
                         spacers=[0, 0])

        layout = [row0, row1]
        return layout

_widget_set_indices = ("widgets_per_row", "width", "height")
_WidgetSetSpecs = namedtuple("WidgetSetSpecs", _widget_set_indices)

transaction_specs = TransactionWidgetSpecs()
button_specs = ButtonWidgetSpecs()

set_specs = _WidgetSetSpecs(widgets_per_row=3, width=0, height=0)


