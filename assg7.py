prefix=int(input("Enter the prefix: "))

subnet=""
for i in range(1,33):
    if i<=prefix:
        subnet=subnet+'1'
    else:
        subnet=subnet+'0'
    if i%8==0 and i>1 and i<32:
        subnet=subnet+'.'
print(subnet)
snm=""
sn=subnet.split('.')
l=len(sn)
for i in range(l):
    part=str(int(sn[i],2))
    #print(part)
    #snm=snm+part
    if i==l-1:
        snm=snm+part
    else:
        snm=snm+part+'.'
print(snm)
