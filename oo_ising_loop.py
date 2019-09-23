from ising_class import*
Temp=0.5   #Temperature
n=20       #Sites per edge for nxn system
ntrials=500000    #number trials
nequil=100000    #equilibration steps

ising1=ising(Temp, n)
ising1.randomize()
while Temp<4.:
    ising1.changeTemp(Temp)
    ising1.trials(nequil)
    ising1.resetprops()
    for i in range(ntrials):
        ising1.trial()
        ising1.addprops()
    ising1.calcprops()
    Temp+=.2
ising1.printsys()
