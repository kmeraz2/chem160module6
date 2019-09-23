from ising_class import*
acell=cell(3,3,10) #Arga: i, j, n
print(acell.cellspin())
acell.spin.flip() #reaching through cell to inner spin object
print (acell.left)#directly acessing the neighbor indices
print(acell.right)
print(acell.up)
print(acell.down)
