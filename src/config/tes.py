from logs import log
import inspect
from bokeh.layouts import row, column
from bokeh.models.widgets import Paragraph, Div
from bokeh.models.layouts import WidgetBox, Spacer
from bokeh.models.widgets.tables import DataTable
from bokeh.plotting import show, curdoc



x = DataTable()

from datetime import date
from random import randint
import bokeh
import bokeh.plotting

data = dict(dates=[i for i in range(10)],
            downloads=[randint(0, 100) for i in range(10)])

source = bokeh.models.ColumnDataSource(data)

columns = [bokeh.models.TableColumn(field="dates", title="Date"),
           bokeh.models.TableColumn(field="downloads", title="Downloads")]

source.callback = bokeh.models.CustomJS(args=dict(source=source), code="""
       console.log( '#Selected rows:');
       var indices = source.selected["1d"].indices;
       for (var i = 0; i<indices.length; i++){
           console.log(i+":"+indices[i]);
       }
       """)

data_table = bokeh.models.DataTable(source=source, columns=columns,
                                    width=400, height=280, editable=True)




data = dict(dates=[i for i in range(10)],
            downloads=[randint(0, 100) for i in range(10)], index=[i+12 for i
                                                                   in range(10)])

source = bokeh.models.ColumnDataSource(data)

columns = [bokeh.models.TableColumn(field="dates", title="Date"),
           bokeh.models.TableColumn(field="downloads", title="Downloads"),
           bokeh.models.TableColumn(field="index", title="INDEX")]
#
# source.callback = bokeh.models.CustomJS(args=dict(source=source), code="""
#        console.log( '#Selected rows:');
#        var indices = source.selected["1d"].indices;
#        for (var i = 0; i<indices.length; i++){
#            console.log(i+":"+indices[i]);
#        }
#        """)

# data_table = bokeh.models.DataTable(source=source, columns=columns,
#                                     width=400, height=280,
#                                     index_header='I_HEADER')

data_table = bokeh.models.DataTable(source=source, columns=columns,
                                    width=400, height=280, index_position=None)

show(data_table)