import mesa
print(f"Mesa version: {mesa.__version__}")

import seaborn as sns
import numpy as np
import pandas as pd
from mesa.visualization import SolaraViz, make_plot_component, make_space_component

"""
Agente libre: Rojo
Agente ocupado: Morado
Caja: Cafe
Pallet: Verde
"""





class RobotAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
           
        # Propiedades necesarias para el ejercicio
        self.isCarrying = False
        self.Box = None
    
    # Lista de pasos a seguir en cada tick
    def step(self):
        self.move()
        # Despues de moverse, revisa si no esta cargando nada, despues revisa si hay algo que pueda cargar
        if not self.checkIfCarrying(): # No hay caso en que revise si puede dejar algo si no esta cargando nada
            self.checkCanPickUp() # Revisa si existe algo para cargar, en caso de que el check anterior sea falso
        self.canDropOff()
                
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
       
        if self.isCarrying:
            self.model.grid.move_agent(self.Box, new_position)
        
    def checkIfCarrying(self):
        """
        Revisa si el robot esta cargando algo, si esta cargando algo ignora todos los contenidos de la celda
        """
        return self.isCarrying
         
            
    def checkCanPickUp(self):
        """
        Ensures there is a box that can be picked up. The robot cannot pick up pallets.
        """
        things = self.model.grid.get_cell_list_contents([self.pos])
        things = [thing for thing in things if thing != self]  # Remove the robot itself

        if len(things) > 0:
            # The robot cannot pick up pallets
            if any(isinstance(thing, PalletObject) for thing in things):
                return False

            for thing in things:
                if isinstance(thing, BoxObject) and not thing.isCarried:  # Check if the box is not already carried
                    self.Box = thing
                    self.isCarrying = True
                    thing.isCarried = True  # Mark the box as being carried
                    break

        return False  # Return False if no box is available to pick up


    def canDropOff(self):
        """
        Check if the robot can drop off the box. A pallet must be present in the current cell.
        """
        if self.isCarrying:  # Only check if the robot is carrying a box
            things = self.model.grid.get_cell_list_contents([self.pos])
            things = [thing for thing in things if thing != self]  # Remove the robot itself

            # Check if a pallet is in the same cell
            if any(isinstance(thing, PalletObject) for thing in things):
                self.dropOff()  # Proceed to drop off the box
                return True

        return False


    def dropOff(self):
        """
        Drop off the box on the pallet and check if it was successfully dropped off.
        """
        # Place the box back on the grid
        self.model.grid.place_agent(self.Box, self.pos) 
        self.Box.isCarried = False  # Mark the box as no longer being carried
        self.isCarrying = False  # Mark the robot as no longer carrying the box
        self.Box = None  # Reset the reference to the box
        
        # Check if a pallet is in the same cell
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        pallet_found = False
        for thing in cell_contents:
            if isinstance(thing, PalletObject):
                pallet_found = True
                thing.Boxes += 1  # Increment the box count on the pallet
                break

        # Post-drop check: Verify if the box is on a pallet
        if pallet_found:
            #self.Box.isCarried = False
            self.isCarrying = False
            self.Box = None
            print(f"Box successfully dropped off at {self.pos}")
        else:
            print("Drop-off failed. No pallet found.")


class BoxObject(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.isCarried = False
       
                
    def checkIfCarried(self):
        
        things = self.model.grid.get_cell_list_contents([self.pos])
        for thing in things:
            if thing.__class__.__name__ == "RobotAgent":
                if not thing.isCarrying:
                    self.isCarried = True
                    return True
        return False
    
        

    # ... rest of your BoxObject class implementation

class PalletObject(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.Boxes = 0

    # ... rest of your PalletObject class implementation


class ShopModel(mesa.Model):
    def __init__(self, N=10, B=5, P=1, width = 10, height = 10, seed=None):
        super().__init__(seed=seed)
        self.num_robot = N
        self.num_boxes = B
        self.num_pallets = P
        #self.schedule = mesa.RandomActivation(self)
        # **Crucially, initialize the grid object here**
        self.grid = mesa.space.MultiGrid(width, height, True)

        

        # Create agents
        for i in range(self.num_robot):
            a = RobotAgent(self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Create boxes
        for i in range(self.num_boxes):
            a = BoxObject(self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Create pallets
        for i in range(self.num_pallets):
            a = PalletObject(self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        
        self.datacollector = mesa.DataCollector(
            agent_reporters={"Pos": "Pos"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")

def agent_portrayal2(agent):
    # Default size and color
    size = 100
    color = "tab:gray"  # Default color for agents

    # RobotAgent: Green if carrying a box, Red if not
    if isinstance(agent, RobotAgent):
        size = 250  # Larger size for RobotAgent
        if agent.isCarrying:
            color = "tab:purple"  # Robot carrying a box is green
        else:
            color = "tab:red"  # Robot not carrying a box is red

    # BoxObject: Always brown and smaller size
    elif isinstance(agent, BoxObject):
        size = 70  # Smaller size for boxes
        color = "tab:brown"  # Box is always brown

    # PalletObject: Always green with a default size
    elif isinstance(agent, PalletObject):
        size = 180  # Default size for pallets
        color = "tab:green"  # Pallet is always green

    return {"size": size, "color": color}



model_params2 = {
    "N": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "B": {
        "type": "SliderInt",
        "value": 20,
        "label": "Number of boxes:",
        "min": 10,
        "max": 30,
        "step": 1,
    },
    "P": {
        "type": "SliderInt",
        "value": 5,
        "label": "Number of pellets:",
        "min": 1,
        "max": 10,
        "step": 1,
    },

    "width": 10,
    "height": 10,
}

model2 = ShopModel(10,5,5)

SpaceGraph = make_space_component(agent_portrayal2)

page = SolaraViz(
    model2,
    components=[SpaceGraph],
    model_params=model_params2,
    name="Culikitakati",
)

page