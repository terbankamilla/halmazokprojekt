reggeli = {"vaj" ,  "tea" , "pirítós"}
reggeli.add("víz")
reggeli.discard('körte')
print(reggeli)

#ebed = set ()
# ebed= set(['halászlé', "kenyér", True])
# print(type(ebed))
# print(ebed)

##2
reggeli = {"vaj" ,  "tea" , "pirítós"}
ebed= {'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

gyumolcskosar= ["eper" , "alma" , "szilva" , "eper"]
fajta= set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)
