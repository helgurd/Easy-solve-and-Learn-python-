
# maping lists to dic 
c=['Ireland', 'UK', 'Germany'] # contry names 
t=['Dublin', 'London', ' Bon'] # City names
ct={} #  c and t lists will maped to dic tc 
y=0
for i in c:
    ct[i]=t[y]
    y=y+1
print(ct) 
    