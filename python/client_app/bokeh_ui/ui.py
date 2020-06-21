from bokeh.layouts import row, column
import inspect

from config.global_config import FigSpecs
from config.global_config import FigureNames as FigNms
from .figures.individual_figure import IndividualFigure, ConsoleOutput, \
    ResourceRatioTable, ItemPropertiesTable, ItemCostTable
from .widgets.individual import TransactionWidget, ButtonWidget
import grpc
import itertools
from global_config import FigureNames, Res, Prod
import grpc_pb2_grpc
from grpc_ui_adapter import GrpcUIAdapter

class UI:
    def __init__(self, portno="50051"):
        """
        UI_callback: Takes in as input (<Func:...>, (args)), return as output
        a dict that is used to update figure_set.
        """
        self.portno = portno
        self.FigInstances = dict()
        self.transaction_widget = TransactionWidget(self.ui_callback)
        self.button_widget = ButtonWidget(self.ui_callback)
        self._init_figures()
        self._couple_range()
        self.ui_layout = self.plot()

    def _init_figures(self):
        call = dict()
        call['command'] = 'init'
        self.ui_callback(call)

    def _update_figures(self, grpc_obj):
        #     inventory_res
        fields = dict()
        fig_name = FigNms.inventory_res
        for i in Res:
            i = i.name
            fields[i] = [grpc_obj.quantities[i]]
        fields['time'] = [grpc_obj.time]
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = IndividualFigure(fields,
                                                           FigSpecs[fig_name])

        #     inventory_prod
        fields = dict()
        fig_name = FigNms.inventory_prod
        for i in Prod:
            i = i.name
            fields[i] = [grpc_obj.quantities[i]]
        fields['time'] = [grpc_obj.time]
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = IndividualFigure(fields,
                                                           FigSpecs[fig_name])

        #     price_res
        fields = dict()
        fig_name = FigNms.price_res
        for i in Res:
            i = i.name
            fields[i] = [grpc_obj.prices[i]]
        fields['time'] = [grpc_obj.time]
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = IndividualFigure(fields,
                                                           FigSpecs[fig_name])

        #     price_prod
        fields = dict()
        fig_name = FigNms.price_prod
        for i in Prod:
            i = i.name
            fields[i] = [grpc_obj.prices[i]]
        fields['time'] = [grpc_obj.time]
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = IndividualFigure(fields,
                                                           FigSpecs[fig_name])

        #     budget
        fields = dict()
        fig_name = FigNms.budget
        fields['budget'] = [grpc_obj.budget]
        fields['time'] = [grpc_obj.time]
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = IndividualFigure(fields,
                                                           FigSpecs[fig_name])

        # item_cost_table
        fields = dict()
        fig_name = FigureNames.item_cost_table
        fields['Item'] = []
        fields['Movein'] = []
        fields['Moveout'] = []
        fields['Storage'] = []
        for term in itertools.chain(Res, Prod):
            term = term.name
            fields['Item'].append(term)
            fields['Movein'].append(grpc_obj.item_cost[term].movein)
            fields['Moveout'].append(grpc_obj.item_cost[term].moveout)
            fields['Storage'].append(grpc_obj.item_cost[term].storage)
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = ItemCostTable(fields)

        #     item_properties_table
        fields = dict()
        fig_name = FigureNames.item_properties_table
        fields['Item'] = []
        fields['Weight'] = []
        fields['Volume'] = []
        for term in itertools.chain(Res, Prod):
            term = term.name
            fields['Item'].append(term)
            fields['Weight'].append(grpc_obj.weights[term])
            fields['Volume'].append(grpc_obj.volumes[term])
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = ItemPropertiesTable(fields)

        #     res_ratio_table
        ratio = dict()
        fig_name = FigureNames.res_ratio_table
        ratio['Resource'] = [i.name for i in Res]
        for i in Prod:
            i = i.name
            per_prod = []
            for j in Res:
                j = j.name
                per_prod.append(grpc_obj.resource_ratio[i].ratio[j])
            ratio[i] = per_prod
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(fields)
        else:
            self.FigInstances[fig_name] = ResourceRatioTable(fields)

        #     console_output
        fig_name = 'console'
        if fig_name in self.FigInstances:
            self.FigInstances[fig_name].figure_update(grpc_obj.console_output)
        else:
            self.FigInstances[fig_name] = ConsoleOutput(grpc_obj.console_output)


    def _couple_range(self):
        print(list(self.FigInstances.keys()))
        ref_x_range = self.FigInstances[FigNms.inventory_res].figure.x_range
        self.FigInstances[FigNms.inventory_prod].figure.x_range = ref_x_range
        self.FigInstances[FigNms.price_res].figure.x_range = ref_x_range
        self.FigInstances[FigNms.price_prod].figure.x_range = ref_x_range
        self.FigInstances[FigNms.budget].figure.x_range = ref_x_range

    def ui_callback(self, call):
        print(f"UIWrapper.callback called with <{call}>.")
        with grpc.insecure_channel(f'localhost:{self.portno}') as channel:
            stub = grpc_pb2_grpc.ClientPageStub(channel)
            grpc_adapter = GrpcUIAdapter(stub)
            if call['command'] == 'buy':
                output = grpc_adapter.Buy(call['category'], call['quantity'])
            elif call['command'] == 'sell':
                output = grpc_adapter.Sell(call['category'], call['quantity'])
            elif call['command'] == 'make':
                output = grpc_adapter.Make(call['category'], call['quantity'])
            elif call['command'] == 'next':
                output = grpc_adapter.Next()
            elif call['command'] == 'save':
                output = grpc_adapter.Save()
            elif call['command'] == 'load':
                output = grpc_adapter.Load()
            elif call['command'] == 'back':
                output = grpc_adapter.Back()
            elif call['command'] == 'quit':
                output = grpc_adapter.Quit()
            elif call['command'] == 'init':
                output = grpc_adapter.Init()
            else:
                raise Exception(call)
        action = output.action
        if action == "update":
            self._update_figures(output)
        print(f"Success <{action}>.")


    # def _construct_individual_figures(self, couple_range=True):
    #     call = dict()
    #     call['command'] = "init"
    #     tp, action = self.ui_callback(call)
    #     if action == 'pause':
    #         return self.FigInstances
    #
    #     inv_res = IndividualFigure(tp[FigNms.inventory_res],
    #                                FigSpecs[FigNms.inventory_res])
    #     inv_prod = IndividualFigure(tp[FigNms.inventory_prod],
    #                                 FigSpecs['inventory_prod'])
    #     pr_res = IndividualFigure(tp[FigNms.price_res],
    #                               FigSpecs['price_res'])
    #     pr_prod = IndividualFigure(tp[FigNms.price_prod],
    #                                FigSpecs['price_prod'])
    #     budget = IndividualFigure(tp[FigNms.budget], FigSpecs['budget'])
    #     # couple range
    #     if couple_range:
    #         ref_x_range = inv_res.figure.x_range
    #         inv_prod.figure.x_range = ref_x_range
    #         pr_res.figure.x_range = ref_x_range
    #         pr_prod.figure.x_range = ref_x_range
    #         budget.figure.x_range = ref_x_range
    #
    #     console = ConsoleOutput(tp[FigNms.console_output])
    #     ratio_t = ResourceRatioTable(tp[FigNms.res_ratio_table])
    #     prop_t = ItemPropertiesTable(tp[FigNms.item_properties_table])
    #     cost_t = ItemCostTable(tp[FigNms.item_cost_table])
    #
    #     FigInsts = [inv_res, inv_prod, pr_res, pr_prod, budget, console,
    #                 ratio_t, prop_t, cost_t]
    #     return FigInsts

    def figure_update(self, tp):
        # log(tp, inspect.currentframe())
        for FigInstance in self.FigInstances:
            value = tp[FigInstance.name]
            if value is not None:
                FigInstance.figure_update(value)
        return True

    # def reload(self, new_data):
    #     self.FigInstances = self._construct_individual_figures(new_data)
    #     self.transaction_widget = TransactionWidget(self.widget_callback)
    #     self.button_widget = ButtonWidget(self.widget_callback)
    #     self.ui_layout = self.plot()

    def plot(self):
        figures_per_row = 3
        row_layouts = []
        tmp_row = []
        for figure in self.FigInstances.values():
            tmp_row.append(figure.figure)
            if len(tmp_row) == figures_per_row:
                row_layouts.append(row(*tmp_row))
                tmp_row = []
        if tmp_row:
            row_layouts.append(row(*tmp_row))
        layout_f = column(*row_layouts)
        layout_w = row(self.transaction_widget.layout, self.button_widget.layout)
        layout_main = column(layout_f, layout_w)
        return layout_main
