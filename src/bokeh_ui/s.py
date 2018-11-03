import pandas as pd

from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL, IBM, MSFT, GOOG
from bokeh.models import ColumnDataSource

p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
p.title.text = 'Click on legend entries to hide the corresponding lines'

for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    cds = ColumnDataSource.from_df(df)
    new_CDS = dict()
    for key, value in cds.items():
        if key == 'date':
            key = key + "_" + name
        new_CDS[key] = list(value)

    # p.line('date_' + name, 'close', line_width=2, color=color, alpha=0.8,
    #        legend=name, source=new_CDS)
    p.line('date_' + name, 'close', line_width=2, color=color, alpha=0.8,
           legend='date_' + name, source=new_CDS)

p.legend.location = "top_left"
p.legend.click_policy="hide"

output_file("interactive_legend.html", title="interactive_legend.py example")

show(p)