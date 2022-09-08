import time
def esquentar_agua():
    return "Agua quente"

def colocar_po():
    return "Coloquei po"

def coar():
    return "Cafe coado"

def fazer_cafe():
    start = time.time()
    
    esquentar_agua()
    time.sleep(100)
    
    colocar_po()
    coar()
    time.sleep(50)

    end = time.time()
    
    calculo_tempo = end - start
    return f"Cafe servido {calculo_tempo}"


    