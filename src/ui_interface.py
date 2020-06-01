from global_config import Res, Prod, FigureNames
from bokeh_ui.ui import UI
import grpc
import grpc_pb2_grpc
import itertools

# todo: for now, discard any function that requires 'reload'
from grpc_ui_adapter import GrpcUIAdapter
import init_values

class UIInterface:
    def __init__(self, port_no="50051"):
        self.port_no = port_no
        self.ui = UI(self.callback)

    def callback(self, call):
        print(f"UIWrapper.callback called with <{call}>.")
        with grpc.insecure_channel(f'localhost:{self.port_no}') as channel:
            stub = grpc_pb2_grpc.UITransferStub(channel)
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
        output = self._convert_to_callback_output(output)
        print(f"Success <{action}>.")
        return output, action

    def _convert_to_callback_output(self, grpc_obj):
        output = dict()

        init_val = init_values.InitValues()
        fields = dict()
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
        output[FigureNames.item_cost_table] = fields

        #     item_properties_table
        fields = dict()
        fields['Item'] = []
        fields['Weight'] = []
        fields['Volume'] = []
        for term in itertools.chain(Res, Prod):
            term = term.name
            fields['Item'].append(term)
            fields['Weight'].append(init_val.inventory['weight'][term])
            fields['Volume'].append(init_val.inventory['volume'][term])
        output[FigureNames.item_properties_table] = fields

        #     res_ratio_table
        ratio = dict()
        ratio['Resource'] = [i.name for i in Res]
        for i in Prod:
            i = i.name
            per_prod = []
            for j in Res:
                j = j.name
                per_prod.append(grpc_obj.resource_ratio[i].ratio[j])
            ratio[i] = per_prod

        output[FigureNames.res_ratio_table] = ratio

        #     console_output
        output[FigureNames.console_output] = grpc_obj.console_output

        #     inventory_res
        fields = dict()
        for i in Res:
            i = i.name
            fields[i] = [grpc_obj.quantities[i]]
        fields['time'] = [grpc_obj.time]
        output[FigureNames.inventory_res] = fields

        #     inventory_prod
        fields = dict()
        for i in Prod:
            i = i.name
            fields[i] = [grpc_obj.quantities[i]]
        fields['time'] = [grpc_obj.time]
        output[FigureNames.inventory_prod] = fields

        #     price_res
        fields = dict()
        for i in Res:
            i = i.name
            fields[i] = [grpc_obj.prices[i]]
        fields['time'] = [grpc_obj.time]
        output[FigureNames.price_res] = fields

        #     price_prod
        fields = dict()
        for i in Prod:
            i = i.name
            fields[i] = [grpc_obj.prices[i]]
        fields['time'] = [grpc_obj.time]
        output[FigureNames.price_prod] = fields

        #     budget
        output[FigureNames.budget] = dict()
        output[FigureNames.budget]['budget'] = [grpc_obj.budget]
        output[FigureNames.budget]['time'] = [grpc_obj.time]
        return output


