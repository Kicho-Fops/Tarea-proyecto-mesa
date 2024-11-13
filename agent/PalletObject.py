# Separo los objetos por concepto de SOLID, donde 1 archivo se encarga de solo 1 clase

# Esta clase solo existe para que los demas agentes la puedan detectar


import mesa

class PalletObject(mesa.Agent):
        
        def __init__(self, unique_id, model):
 
            self.Boxes = 0 # Numero de cajas en el pallet
        
            
        