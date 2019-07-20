
# multi D Array/Lists imbeded inside for lops 

###version 1 returninng in form of table and in range of soem number
#...................................................................
# many_grids= int(input('please input your number here '))
# many_grids1= int(input('please input second number here'))
# allArrays =[[0 for row in  range (many_grids)] for col in range(many_grids1)]
# for row in range(many_grids):
#     for col in range(many_grids1):
#         allArrays[col][row] = row*col
# print(allArrays)

 
###version2
#.....................................................................  
staffs = [['Helgurd',44], ['Adam',35], ['Rez',18]]
   
for a,b in staffs:
    print ('your name is ',a ,'your age',int(b) )
           
