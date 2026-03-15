from .Environment import Environment


Level1 = Environment(1, "Single Line on Top", (12,12), ((5,3)), enclosed = False)
Level1.field[:,11]=1

Level2 = Environment(2, "Top right corner + Start below Wall", (12,12), ((1,8)), enclosed = False)
Level2.field[:,11]=1
Level2.field[11,:]=1

Level3 = Environment(3, "Full Box", (12,12), ((1,8)))

Level4 = Environment(4, "Single Block Corner", (12,12), ((5,0)))
Level4.field[0:3,5:12]=1

Level5 = Environment(5, "Inner and Outer Agent", (12,12), ((3,0), (5,1)))
Level5.field[3:6,5:8]=1

Level6 = Environment(6, "Complex Environment with Sharp Corners", (12,12), ((1,4), (10,4)))
Level6.field[0,0:2]=1
Level6.field[0:2,-1]=1
Level6.field[-2:,-1]=1
Level6.field[-3:,-4]=1
Level6.field[0:3,-4]=1
Level6.field[-1,0:2]=1
Level6.field[4,0:5]=1
Level6.field[-5,0:5]=1
Level6.field[3,4]=1
Level6.field[-4,4]=1

Level7 = Environment(7, "Impossible?", (12,12), ((5,2)), tight=True)
Level7.field[4:7,5]=1
Level7.field[4,5:9]=1
Level7.field[6,5:9]=1

levels = [Level1, Level2, Level3, Level4, Level5, Level6, Level7]
