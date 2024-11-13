
import mesa
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from agent.RobotAgent import RobotAgent
from agent.BoxObject import BoxObject
from agent.PalletObject import PalletObject


class ShopModel(mesa.Model):
    
    def __init__(self, N, B, P, width, height):
        self.num_robot = N
        self.num_boxes = B
        self.num_pallets = P
        self.schedule = mesa.RandomActivation(self)
        self.grid = mesa.MultiGrid(width, height, True)
        
        # Crear los Agentes
        
        # Crear agente de robot
        for i in range(self.num_robot):
            a = RobotAgent(i, self, N, width, height)
            self.schedule.add(a)
            
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                
                # Verificar si hay robots en la celda
                cell_contents = self.grid.get_cell_list_contents((x, y))
                if not any(isinstance(agent, RobotAgent) for agent in cell_contents):
                    self.grid.place_agent(a, (x, y))
                    break
        
        # Crear agente de cajas
        for i in range(self.num_boxes):
            a = BoxObject(i, self)
            self.schedule.add(a)
            
            # Ayuda de chatGPT para evitar que las cajas se coloquen en la misma celda
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                
                # Verificar si hay cajas en la celda
                cell_contents = self.grid.get_cell_list_contents((x, y))
                if not any(isinstance(agent, BoxObject) for agent in cell_contents):
                    self.grid.place_agent(a, (x, y))
                    break
        
        # Crear agente de pallets
        for i in range(self.num_pallets):
            a = PalletObject(i, self)
            
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                
                # Verificar si hay pallets en la celda
                cell_contents = self.grid.get_cell_list_contents((x, y))
                if not any(isinstance(agent, PalletObject) for agent in cell_contents):
                    self.grid.place_agent(a, (x, y))
                    break
        
    def step(self):
        self.schedule.step()
        
        
           
