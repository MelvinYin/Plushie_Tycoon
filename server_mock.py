import grpc
import grpc_pb2
import grpc_pb2_grpc
from global_config import Res, Prod
from config import init_values
from config import properties

from concurrent.futures import ThreadPoolExecutor
import itertools

class MockServer(grpc_pb2_grpc.UITransferServicer):
    def __init__(self):
        self.curr_count = 0
        self.curr_sign = -1

    def default_return(self, action="update"):
        addition = self.curr_count * self.curr_sign
        initials = init_values.InitValues()
        prices = dict()
        quantities = dict()
        weights = dict()
        volumes = dict()
        item_cost = dict()
        budget = initials.budget
        time = initials.time
        console_output = f"Mock callback {self.curr_sign}|{self.curr_count}"
        tier = 0
        movein_factor = properties.WarehouseStats.movein_cost[tier]
        moveout_factor = properties.WarehouseStats.moveout_cost[tier]
        storage_factor = properties.WarehouseStats.store_cost[tier]
        for i in itertools.chain(Res, Prod):
            i = i.name
            assert i in initials.market, f"{i} not in initials.market"
            assert i in initials.inventory, f"{i} not in initials.market"
            assert i in initials.inventory[
                'weight'], f"{i} not in initials.market['weight']"
            assert i in initials.inventory[
                'volume'], f"{i} not in initials.market['volume']"

            prices[i] = initials.market[i] + addition
            quantities[i] = initials.inventory[i] + addition
            weights[i] = initials.inventory['weight'][i]
            volumes[i] = initials.inventory['volume'][i]
            movein = movein_factor.weight * weights[i] + movein_factor.volume\
                     * \
                     volumes[i]

            moveout = moveout_factor.weight * weights[
                i] + moveout_factor.volume * volumes[i]

            storage = storage_factor.weight * weights[
                i] + storage_factor.volume * volumes[i]

            item_cost[i] = grpc_pb2.mItemCost(movein=movein, moveout=moveout,
                                              storage=storage)
        resource_ratio = dict()
        for i in Prod:
            i = i.name
            per_p = dict()
            for j in Res:
                j = j.name
                per_p[j] = initials.production['res_ratio'][i][j]
            resource_ratio[i] = grpc_pb2.mRatioPerProduct(ratio=per_p)
        output_object = grpc_pb2.UserOutput(prices=prices,
                                            quantities=quantities,
                                            item_cost=item_cost,
                                            resource_ratio=resource_ratio,
                                            console_output=console_output,
                                            budget=budget, time=time,
                                            action=action, weights=weights,
                                            volumes=volumes)
        return output_object

    def Buy(self, request, context):
        print(f"Buy called with {request.name} and {request.quantity}.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Sell(self, request, context):
        print(f"Sell called with {request.name} and {request.quantity}.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Make(self, request, context):
        print(f"Make called with {request.name} and {request.quantity}.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Next(self, request, context):
        print(f"Next called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Save(self, request, context):
        print(f"Save called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("pause")

    def Load(self, request, context):
        print(f"Load called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Back(self, request, context):
        print(f"Back called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")

    def Quit(self, request, context):
        print(f"Quit called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("pause")

    def Init(self, request, context):
        print(f"Init called.")
        self.curr_count += 1
        self.curr_sign *= -1
        return self.default_return("update")


def run():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_UITransferServicer_to_server(MockServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run()
