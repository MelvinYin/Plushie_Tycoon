##############################################################################
# Widget Specs

from collections import namedtuple
from enum import Enum, auto, unique

##############################################################################
# Global
try:
    from base import Res, Prod, Func, res_members, prod_members
except:
    from .base import Res, Prod, Func, res_members, prod_members

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
        labelmap[Func.buy] = "Buy"
        labelmap[Func.sell] = "Sell"
        labelmap[Func.make] = "Make"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Func.buy, Func.sell, Func.make],
                   labelmap = labelmap)
        return RBG

    def set_RBG2(self):
        labelmap = dict()
        labelmap[Res] = "Res"
        labelmap[Prod] = "Prod"
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=[Res, Prod],
                   labelmap = labelmap)
        return RBG

    def set_RBG3(self):
        labelmap = dict()
        labelmap[Res.cloth] = "cloth"
        labelmap[Res.stuff] = "stuff"
        labelmap[Res.accessory] = "accessory"
        labelmap[Res.packaging] = "packaging"
        labelmap[Prod.aisha] = "aisha"
        labelmap[Prod.beta] = "beta"
        labelmap[Prod.chama] = "chama"
        # noinspection PyTypeChecker
        assert len(labelmap) == len(res_members) + len(prod_members)
        RBG_ = namedtuple("RBG", 'width height labels labelmap')
        RBG = RBG_(width=400,
                   height=17,
                   labels=res_members,
                   labelmap=labelmap)
        return RBG

    def set_TI(self):
        TI_ = namedtuple("Header", 'width height placeholder')
        TI = TI_(width=1,  # Text box
                 height=1,
                 placeholder='Quantity')
        return TI

    def set_button(self):
        Button = namedtuple("Header", 'width height label')
        button = Button(width=50,  # Size of button
                        height=0,
                        label="Send")
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
        labelmap[Func.next] = "next"
        labelmap[Func.save] = "save"
        labelmap[Func.load] = "load"
        labelmap[Func.quit] = "quit"
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
                        label="Send")
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

class WidgetSetSpecs:
    def __init__(self):
        self.widgets_per_row = 3
        self.width = 0
        self.height = 0

class WidgetIndividualSpecs:
    def __init__(self):
        self.transaction_1 = TransactionWidgetSpecs()
        self.button_1 = ButtonWidgetSpecs()

class WidgetSpecs:
    def __init__(self):
        self.set = WidgetSetSpecs()
        self.widget = WidgetIndividualSpecs()












