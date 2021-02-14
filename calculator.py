stock=input("stock: ")
p=float(input("Precio_Compra: "))

fg=.000075
smv=.000135
sab=float(input("comision_SAB: "))
minSAB=float(input("minimo_SAB: "))

minCAV=5

capital=float(input("capital: "))
IBGC=["ALICORC1","ALICORI1","BBVAC1","CPACASC1","CPAC",
"BUENAVC1","BVN","ENGIEC1","FERREYC1","INRETC1","IFS","RIMSEGC1"
]

if stock in IBGC:
    cavali=.00004095
else:
    cavali=.0004095

if stock in IBGC:
    bvl=.000021
else:
    bvl=.00021

caso1=(capital*p*sab)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))
caso2=(capital*p*cavali)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))

if (caso1>minSAB and caso2>minCAV):
    acciones=capital/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab+1.18*cavali))
    acciones=round(acciones-0.5)
    print(acciones)

caso3=(sab*p*(capital-1.18*(minSAB)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))
caso4=(cavali*p*(capital-1.18*(minSAB)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))

if (caso3<minSAB and caso4>minCAV):
    acciones=(capital-1.18*minSAB)/(p*(1+1.18*bvl+1.18*fg+smv+1.18*cavali))
    acciones=round(acciones-0.5)
    print(acciones)

caso5=(sab*p*(capital-1.18*(minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))
caso6=(cavali*p*(capital-1.18*(minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))

if (caso5>minSAB and caso6<minCAV):
    acciones=(capital-1.18*(minCAV))/(p*(1+1.18*bvl+1.18*fg+smv+1.18*sab))
    acciones=round(acciones-0.5)
    print(acciones)

caso7=(sab*p*(capital-1.18*(minSAB+minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv))
caso8=(cavali*p*(capital-1.18*(minSAB+minCAV)))/(p*(1+1.18*bvl+1.18*fg+smv))

if (caso7<minSAB and caso8<minCAV):
    acciones=(capital-1.18*(minSAB+minCAV))/(p*(1+1.18*bvl+1.18*fg+smv))
    acciones=round(acciones-0.5)
    print(acciones)


invertido=p*acciones*(1+1.18*bvl+1.18*fg+smv)+1.18*max(sab*p*acciones,minSAB)+1.18*max(cavali*p*acciones,minCAV)
invertido=round(invertido,2)
print(invertido)
saldo=capital-invertido
saldo=round(saldo,2)
print(saldo)