import mesa
print(f"Mesa version: {mesa.__version__}")

import seaborn as sns
import numpy as np
import pandas as pd
from mesa.visualization import SolaraViz, make_plot_component, make_space_component

import os
import sys
from IPython.display import display

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from agent.RobotAgent import RobotAgent
from agent.BoxObject import BoxObject
from agent.PalletObject import PalletObject

from model.ShopModel import ShopModel


# Crear la visualizacion

width = 10
height = 10

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    
    if type(agent) is RobotAgent:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
        
    elif type(agent) is BoxObject:
        portrayal["Color"] = "brown"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
        
    elif type(agent) is PalletObject:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.5
    
    return portrayal

# grid = mesa.visualization.CanvasGrid(agent_portrayal, width, height, 500, 500)

model_params = { "N": 5, "B": 20, "P": 5, "width": width, "height": height }

SpaceGraph = make_space_component(agent_portrayal)
#GiniPlot = make_plot_component("Gini")

page = SolaraViz(
    ShopModel,
    components=[SpaceGraph],
    model_params=model_params,
    name="Porfavor sirve :(",
)

# server = ModularServer(ShopModel,
#                                             [grid],
#                                             "Modelo de tienda",
#                                             {"N": 5, "B": 20, "P": 5, "width": width, "height": height})
    
    
# server.port = 8521
# server.launch()

# Set the server port and launch the server



display(page)

