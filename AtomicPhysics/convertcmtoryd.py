file = open('energiestoconvert')
convfile = open('energylevelsconv','w')
convert = (1/13.606)
for i in file:
    print(i.split()[-1])
    num = round(float(i.split()[-1])*convert,4)
    print(num)
    convfile.write(str(num)+'\n')
convfile.close()
file.close()
