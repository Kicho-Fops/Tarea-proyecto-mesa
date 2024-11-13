# Separo los objetos por concepto de SOLID, donde 1 archivo se encarga de solo 1 clase

# Esta clase solo existe para que los demas agentes la puedan detectar

import mesa




class BoxObject(mesa.Agent):
        
        def __init__(self, unique_id, model):
            
            self.isCarried = False
        
        def step(self):
            if (self.checkIfCarried()):
                self.move()
                
        def checkIfCarried(self):
            
            things = self.model.grid.get_cell_list_contents([self.pos])
            for thing in things:
                if thing.__class__.__name__ == "RobotAgent":
                    if thing.isCarrying:
                        self.isCarried = True
                        return True
            return False
        
        