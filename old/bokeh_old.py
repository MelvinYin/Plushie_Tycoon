import matplotlib.pyplot as plt

def plot_fn(res_data_as_dict):
    """
    Res-data need to be from long-term storage, as a dict, with keys as
    time_steps
    """
    time_steps, res_data = list(res_data_as_dict.keys()), list(res_data_as_dict.values())
    plt.figure(1)
    count = 0
    prev_point = None
    x_ticks = []
    for i in range(len(time_steps)):
        immediate_res_data = res_data[i]
        add_count = range(count, count + len(immediate_res_data))
        plt.plot(add_count, immediate_res_data, "x-", color="b")
        if prev_point:
            plt.plot([add_count[0]-1, add_count[0]], [prev_point, immediate_res_data[0]], "x-", color="b")
        prev_point = immediate_res_data[-1]
        plt.axvline(add_count[-1],ymin=0, linestyle="dotted", color="k")
        x_ticks.append(add_count[-1])
        count += len(immediate_res_data)

    plt.xticks(x_ticks, [str(i) for i in range(len(x_ticks))])


# res_data_as_dict = dict()
# res_data_as_dict[12] = [134,145,156]
# res_data_as_dict[13] = [178, 189]
# res_data_as_dict[14] = [196,145]
#
# plot_fn(res_data_as_dict)
# plt.show()


from bokeh.plotting import figure, output_file, show, ColumnDataSource
import itertools
from bokeh.models.tickers import AdaptiveTicker
from bokeh.models import HoverTool

def add_time_step_vlines(p, time_steps, min_val=0, max_val=10):
    xs = [[i, i] for i in time_steps]
    ys = [i for i in itertools.repeat([min_val, max_val], times=len(time_steps))]
    p.multi_line(xs=xs, ys=ys, color='red', line_dash="dotted")
    return True

def add_dict_plot(p, data):
    """
    For current way of representing time_steps:
    Pros: Provides a proportional sense of evolution as a function of time.
    Cons: Difficult to see if steps have many actions.
    :param p:
    :param data:
    :return:
    """
    xs = []
    ys = []
    for key, val in data.items():
        if key != "col_names":
            val = [i for i in val if i]
            xs.append([int(key) + i/len(val) for i in range(len(val))])
            ys.append(val)

    p.multi_line(xs, ys)
    assert len(xs) == len(ys)
    for i in range(len(xs)):
        for j in range(len(xs[i])):
            assert len(xs[i]) == len(ys[i])
            p.x(xs[i][j], ys[i][j], size=10, name="points")

    connecting_xs = []
    connecting_ys = []
    for i in range(len(xs)-1):
        connecting_xs.append([xs[i][-1], xs[i+1][0]])
        connecting_ys.append([ys[i][-1], ys[i+1][0]])
    p.multi_line(connecting_xs, connecting_ys)
    return True



output_file("line.html")
res_data_as_dict = dict()
res_data_as_dict[str(12)] = [134,145,156]
res_data_as_dict[str(13)] = [178, 189, 'nan']
res_data_as_dict[str(14)] = [196,145, 'nan']
res_data_as_dict["col_names"] = []
for key in res_data_as_dict.keys():
    if key != "col_names":
        res_data_as_dict["col_names"].append("A" + key + "A")
res_data_as_dict = ColumnDataSource(data=res_data_as_dict)
print(res_data_as_dict.data)

hover = HoverTool(tooltips=[
    ("Point No.", "$index"),
    ("Time Step", "@col_names")], names=["points"])

p = figure(plot_width=400, plot_height=400, tools=[hover])

p.title.text = "Placeholder"
p.title.align = 'center'
p.xaxis.axis_label="Time Steps"
p.yaxis.axis_label="Placeholder"
p.xgrid.ticker=AdaptiveTicker(min_interval=1, num_minor_ticks=0)
p.xaxis.ticker=AdaptiveTicker(min_interval=1, num_minor_ticks=0)
add_time_step_vlines(p, res_data_as_dict.column_names)
add_dict_plot(p, res_data_as_dict.data)
show(p)

# def generate_line_data(res_data_as_dict):
#     keys = res_data_as_dict.keys()
#     xs = [[i, i] for i in keys]
#     val = []
#     for i in res_data_as_dict.values():
#         for j in i:
#             val.append(j)
#     min_val = min(val)
#     max_val = max(val)
#     ys = [[min_val, max_val] for _ in range(len(keys))]
#     return xs, ys
#
# from bokeh.plotting import figure, output_file, show
#
# # output to static HTML file
# output_file("line.html")
#
# p = figure(plot_width=400, plot_height=400)
#
# xs, ys = generate_line_data(res_data_as_dict)
#
# p.multi_line(xs, ys, color='red', line_cap="square")
# # print(xs)
# # print(ys)
# # p.multi_line(xs=[[1, 2, 3], [2, 3, 4]], ys=[[6, 7, 2], [4, 5, 7]],
# #              color=['red','green'])
# # show the results
# show(p)

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import CDSView
from bokeh.models.filters import Filter
from bokeh.models.tickers import AdaptiveTicker
from bokeh.models import HoverTool

output_file("line.html")
res_data_as_dict = dict()
res_data_as_dict[str(12)] = [134,145, 156]
res_data_as_dict[str(13)] = [178, 189, 156]
res_data_as_dict[str(14)] = [196,145, 156]

res_data_as_dict["12_x"] = [1,2, 3]
res_data_as_dict["x_13"] = [1,2, 4]
res_data_as_dict["14_x"] = [1,2, 5]
# res_data_as_dict["size"] = [10, 0, 10]

res_data_as_dict = ColumnDataSource(data=res_data_as_dict)
# print(view.dataspecs())

hover = HoverTool(tooltips=[
    ("Point No.", "$index"),
    ("Time Step", "@13")], names=["points"])
p = figure(plot_width=400, plot_height=400, tools=[hover])
p.x("13", "x_13", name="points", source=res_data_as_dict, size=10)

show(p)
# from bokeh.sampledata.iris import flowers
# # print(flowers)













# def generate_line_data(res_data_as_dict):
#     keys = res_data_as_dict.keys()
#     xs = [[i, i] for i in keys]
#     val = []
#     for i in res_data_as_dict.values():
#         for j in i:
#             val.append(j)
#     min_val = min(val)
#     max_val = max(val)
#     ys = [[min_val, max_val] for _ in range(len(keys))]
#     return xs, ys
#
# from bokeh.plotting import figure, output_file, show
#
# # output to static HTML file
# output_file("line.html")
#
# p = figure(plot_width=400, plot_height=400)
#
# xs, ys = generate_line_data(res_data_as_dict)
#
# p.multi_line(xs, ys, color='red', line_cap="square")
# # print(xs)
# # print(ys)
# # p.multi_line(xs=[[1, 2, 3], [2, 3, 4]], ys=[[6, 7, 2], [4, 5, 7]],
# #              color=['red','green'])
# # show the results
# show(p)

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.tickers import FixedTicker


output_file("line.html")
res_data_as_dict = dict()
res_data_as_dict["ff"] = [13,14,16, 34, 2, 3, 2, 5, 6, 2]
res_data_as_dict['x_'] = [0, 0.3, 0.6, 1, 1.5, 2, 3, 4, 5]
res_data_as_dict = ColumnDataSource(data=res_data_as_dict)


p = figure(plot_width=400, plot_height=400)
p.x(x="x_", y="ff", source=res_data_as_dict)

p.title.text = "Placeholder"
p.title.align = 'center'
p.xaxis.axis_label="Time Steps"
p.yaxis.axis_label="Placeholder"
p.xaxis.ticker = FixedTicker(ticks=[0, 1, 2, 3, 4, 5])
# print(dir(FixedTicker))
# print(FixedTicker.document)
show(p)
