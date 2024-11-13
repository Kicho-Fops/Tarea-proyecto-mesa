from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import mesa.visualization
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.ShopModel import ShopModel
from agent.RobotAgent import RobotAgent
from agent.BoxObject import BoxObject
from agent.PalletObject import PalletObject


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

# Crear la visualizacion

width = 10
height = 10

grid = mesa.visualization.CanvasGrid(agent_portrayal, width, height, 500, 500)

server = ModularServer(ShopModel,
                                            [grid],
                                            "Modelo de tienda",
                                            {"N": 5, "B": 20, "P": 5, "width": width, "height": height})
    
server.port = 8521
server.launch()