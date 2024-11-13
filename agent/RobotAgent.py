import mesa
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from agent.BoxObject import BoxObject
from agent.PalletObject import PalletObject

class RobotAgent(mesa.Agent):
    
    def __init__(self, unique_id, model, N, width, height):
        
       
        
        
        # Propiedades necesarias para el ejercicio
        self.isCarrying = False
        self.Box = None
    
    # Lista de pasos a seguir en cada tick
    def step(self):
        self.move()
        # Despues de moverse, revisa si no esta cargando nada, despues revisa si hay algo que pueda cargar
        if(self.checkIfCarrying()): # No hay caso en que revise si puede dejar algo si no esta cargando nada
            self.checkCanPickUp() # Revisa si existe algo para cargar, en caso de que el check anterior sea falso
            self.canDropOff()
                
        
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
       
        if self.is_carrying:
            self.model.grid.move_agent(self.Box, new_position)
        
    def checkIfCarrying(self):
        """
        Revisa si el robot esta cargando algo, si esta cargando algo ignora todos los contenidos de la celda
        """
        if self.isCarrying:
            return True
        else:
            # Si no esta cargando nada, manda a llamar a la funcion que revisa si existe algun objeto valido que pueda cargar
            return self.checkCanPickUp() 
            
        
    def checkCanPickUp(self):
        """
        Asegura que exista una caja que pueda cargar, no puede cargar pallets
        """
        
        things = self.model.grid.get_cell_list_contents([self.pos])
        # Asegurando que no pueda escogerme a mi mismo
        things.pop(things.index(self)) # Obtenido de https://github.com/jeremy-miller/mesa-boltzmann-wealth-model/blob/main/money_model.ipynb
        if len(things) > 0:
            if PalletObject in things:
                return False # Solo puede cargar cajas y no puede recoger cajas de pallets
            for thing in things:
                if isinstance(thing, BoxObject): # Segun Gemini, esto sirve para identificar la caja en especifico y no tomar todos los objeto caja
                    self.Box = thing
                    self.isCarrying = True
                    break
        else:
            return False
                
    def canDropOff(self):
        """
        Revisa si el robot puede dejar lo que esta cargando
        """
        things = self.model.grid.get_cell_list_contents([self.pos])
        # Asegurando que no pueda escogerme a mi mismo
        things.pop(things.index(self))
        
        # Si existe un Pallet, puede dejar la caja
        
        if PalletObject in things: 
            self.dropOff(things)
            return True
        else:
            return False
        
    def dropOff(self, cell):
        """
        Deja la caja en el pallet
        """
        self.model.grid.place_agent(self.Box, self.pos)
        self.isCarrying = False
        self.Box = None
        cell.Boxes += 1
        return True
    