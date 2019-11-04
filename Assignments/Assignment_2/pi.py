def ArchimedesPi():
    
   
    sides = [6, 12, 24, 48, 96, 192]
    
    
    side = 1
    
    for length in sides:
        
        half_side = side/2
        
        pmeter = length * side
       
        a = (1-(half_side**2))**0.5
        b = 1 - a
        
        pi = pmeter / 2
        
        print(pi)
        
        side = ((b**2)+(half_side**2))**0.5
        
ArchimedesPi()