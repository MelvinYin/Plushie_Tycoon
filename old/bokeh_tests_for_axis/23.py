from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, CategoricalScale
from bokeh.plotting import figure

output_file("test.html")

data = dict(a=[1, 2], b=[2, 3])

source = ColumnDataSource(data=data)
p = figure()
p.x_range = FactorRange(*data)
# p.x_scale = CategoricalScale()
p.x(x='a', y='b', source=source, size=10)

show(p)