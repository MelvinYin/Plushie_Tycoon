
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, CategoricalScale
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("bar_nested_colormapped.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']

data = dict(a=[2, 1, 4, 3, 2, 4], b=[1,2,3,4,5,6], c=[1,2,3,4,5,6])


# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]

source = ColumnDataSource(data=data)
data2 = ['a', 'afva', "c", "d", 'e', 'f', 'g']
p = figure(x_range=FactorRange(*data2), plot_height=350, title="Fruit Counts by Year",
           toolbar_location=None, tools="")
# p.x_range = FactorRange(*data2)
# p.x_scale = CategoricalScale()
p.x(x='a', y='b', source=source, size=10)

show(p)