'''def draw_rectangle(width, symbol_ram):
    for i in range(width):
        
        print(symbol_ram)
    
        for j in range(width):
            space = 3
            print(space*" ", symbol_ram)
   
        
    
draw_rectangle(10, "@")'''
def draw_rectagular(w, h, sym_ram, sym_zap):

    for y in range(h):
        
        for x in range(w):
            if y == 0 or y == h - 1 or x == 0 or x==w - 1:
                print(sym_ram, end = "")
            else:
                print(sym_zap, end="")
        print()
        
draw_rectagular(10, 10, "@", "*")