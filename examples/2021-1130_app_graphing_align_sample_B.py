# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:15:16 2021

@author: anthony.krzysko
"""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from xray_scattering_tools.get_detector_objects import get_detector_objects_from_folder
from xray_scattering_tools.get_detector_objects import get_dataframe_from_objects_list
from matplotlib import cm
import matplotlib.colors 


directory_in_str = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1202_sample_B_donut_2"
directory_in_str_graphite = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1202_sample_B_donut_2"
# directory_in_str_2 = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1129_sample_A_two_slit"
# directory_in_str_3 = r"C:\Users\Anthony.Krzysko\Documents\2021-1128_compton_exp_11IDC\data\2021-1130_sample_a_two_slits"

# list of detector objects with relevant data
obj_list = get_detector_objects_from_folder(directory_in_str, "point", angle=88.8)
# obj_list_2 = get_detector_objects_from_folder(directory_in_str_2, "point", angle=89.3)
# obj_list_3 = get_detector_objects_from_folder(directory_in_str_3, "point", angle=89.3)
# obj_list.extend(obj_list_2)
# obj_list.extend(obj_list_3)

for obj in obj_list: 
    if obj.meta_data["scan_name"] == "sample_B_vert_1_downstream":
        obj.meta_data["scan_name"] = "sample B Li downstream"           
    elif obj.meta_data["scan_name"] == "sample_B_vert_1_middle":
        obj.meta_data["scan_name"] = "sample B Li middle"
    elif obj.meta_data["scan_name"] == "sample_B_vert_1_upstream":
        obj.meta_data["scan_name"] = "sample B Li upstream"
        
    elif obj.meta_data["scan_name"] == "sample_B_vert_2_downstream":
        obj.meta_data["scan_name"] = "sample B graphite downstream"
    elif obj.meta_data["scan_name"] == "sample_B_vert_2_middle":
        obj.meta_data["scan_name"] = "sample B graphite middle"
    elif obj.meta_data["scan_name"] == "sample_B_vert_2_upstream":
        obj.meta_data["scan_name"] = "sample B graphite upstream"
        
    elif obj.meta_data["scan_name"] == "sample_B_vert_3_upstream":
        obj.meta_data["scan_name"] = "sample B NMC upstream"
    elif obj.meta_data["scan_name"] == "sample_B_vert_3_middle":
        obj.meta_data["scan_name"] = "sample B NMC middle"
    elif obj.meta_data["scan_name"] == "sample_B_vert_3_downstream":
        obj.meta_data["scan_name"] = "sample B NMC downstream"

    elif obj.meta_data["scan_name"] == "sample_B_donut_pt_A":
        obj.meta_data["scan_name"] = "sample B point A"
    elif obj.meta_data["scan_name"] == "sample_A_pt_2_time_2":
        obj.meta_data["scan_name"] = "sample A 2 slits Li 1 h"
    elif obj.meta_data["scan_name"] == "sample_A_pt_2_time_3":
        obj.meta_data["scan_name"] = "sample A 2 slits Li 20 min"
    elif obj.meta_data["scan_name"] == "sample_A_pt_2_time_4":
        obj.meta_data["scan_name"] = "sample A 2 slits Li 5 min"
        
    elif obj.meta_data["scan_name"] == "sample_A_pt_3_time_1":
        obj.meta_data["scan_name"] = "sample A 2 slits NMC 3 h"
    elif obj.meta_data["scan_name"] == "sample_A_pt_3_time_2":
        obj.meta_data["scan_name"] = "sample A 2 slits NMC 1 h"
    elif obj.meta_data["scan_name"] == "sample_A_pt_3_time_3":
        obj.meta_data["scan_name"] = "sample A 2 slits NMC 20 min"
    elif obj.meta_data["scan_name"] == "sample_A_pt_3_time_4":
        obj.meta_data["scan_name"] = "sample A 2 slits NMC 5 min"
        
        
dataframe = get_dataframe_from_objects_list(obj_list)


def sep_underscore(str_in):
    str_items = str_in.split('_')
    capital_items = []
    for item in str_items:
        capital_items.append(item.capitalize())
    
    capital_str = " "
    return(capital_str.join(capital_items))

def generate_table(dataframe, max_rows=1):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets=['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css']
# external_stylesheets = ['https://codepen.io/ninjakx/pen/bGEpbXo.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.config.serve_locally = False
# app = dash.Dash(__name__)

colors = {
    'background': '#ffffff',
    'text': '#111111'
    
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Compton Data Reduction',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),

    html.Div(
        children=f'Folder Path: {directory_in_str}',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),  
    
    html.Label(["x values"]),
     dcc.Dropdown(
        id='x-values',
        options=[
            {'label': 'Channels', 'value': 'channels'},
            {'label': 'Calibrated Energy', 'value': 'calibrated_energy'},
            {'label': 'Momentrum Array', 'value': 'momentum_array'}
        ],
        value='channels'
    ),
    html.Div(id='dd-output-container'),
      

    html.Label(["y values"]),
     dcc.Dropdown(
        id='y-values',
        options=[
            {'label': 'Raw Intensity', 'value': 'raw_intensity'},
            {'label': 'Cps Intensity', 'value': 'cps_intensity'},
            {'label': 'Norm To Wings Intensity', 'value': 'norm_to_wings_intensity'}
        ],
        value='raw_intensity'
    ),
    html.Div(id='dd-output-container_2'),
    
    html.Label(["plot options"]),
     dcc.Dropdown(
        id='y-scale',
        options=[
            {'label': 'Log y', 'value': "log"},
            {'label': 'Linear y', 'value': "linear"},
        ],
        value='linear'
    ),
     
     html.Div([
         
        dcc.Graph(id='compton_graph')
        
        
    ]),
     
     html.Div([ 
        html.Label(["Region 1"]),
        dcc.Input(id="a", type="number", value=0),
        dcc.Input(id="b", type="number", value=0),
            ]),
     
     html.Div([
        html.Label(["Region 2"]),
        dcc.Input(id="c", type="number", value=0),
        dcc.Input(id="d", type="number", value=0),    
    ]),

    # generate_table(dataframe)
    generate_table(dataframe, dataframe.shape[0])
])


#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='compton_graph', component_property='figure'),
    [Input(component_id='x-values', component_property='value')],
    [Input(component_id='y-values', component_property='value')],
    [Input(component_id='y-scale', component_property='value')],
    [Input(component_id='a', component_property='value')],

)
    
def build_graph(chosen_x, chosen_y, log_lin, val):
    fig = go.Figure() 
    add_count=0
    for obj in obj_list:   
        color = cm.get_cmap('rainbow', len(obj_list))
        fig.add_trace(go.Scatter(
                            x=obj.data_values[chosen_x], 
                            y=obj.data_values[chosen_y],
                            mode='lines',
                            name=obj.meta_data["scan_name"],
                            line=dict(
                            color=matplotlib.colors.rgb2hex(color(add_count)))
                            )
                      )
        add_count+=1
        
        try:
            obj.get_ratio_regions(obj.data_values[chosen_x], obj.data_values[chosen_y], float(val),0,0,0)
            fig.add_trace(go.Scatter(
                            x=obj.data_values["isolated_x_1"],
                            y=obj.data_values["isolated_y_1"],
                            showlegend=False,
                            mode='lines',
                            line=dict(
                            color="black")
                            )
                      )
        except ZeroDivisionError: 
            print("bound cause zero divide")
        
        except TypeError:
            print("type error in bounds")

    fig.update_layout(
        
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        xaxis_title= sep_underscore(chosen_x),
        yaxis_title= sep_underscore(chosen_y),
           
    )    
    
    fig.update_yaxes(type=log_lin)
    dataframe = get_dataframe_from_objects_list(obj_list)
    generate_table(dataframe, dataframe.shape[0])

    return fig

#---------------------------------------------------------------


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="5555")
    

