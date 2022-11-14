#1 
halmaz = { "egy" , "ketto" , "harom" , "negy"}

#2
halmaz2 = halmaz.copy()
halmaz.copy()
print(halmaz2)

#3
halmaz3a={"a","b", "c", "d"}
halmaz3b={"a","b","e","d"}
halmaz3a = halmaz3b.difference()

#4
halmaz4a={"e" ,"f" ,"g"}
halmaz4b={"m" ,"w" ,"q"}
halmaz4a.difference_update(halmaz4b)

#5
halmaz5a={"e" ,"f" ,"g"}
halmaz5b={"m" ,"w" ,"q"}
halmaz5a.intersection(halmaz5b)

#6
halmaz6a={"o" ,"p" ,"t"}
halmaz6b={"k" ,"l" ,"a"}
halmaz6a.intersection_update(halmaz6b)

#7
A = {1, 2, 3, }
B = {4, 5, 6}
print(A.isdisjoint(B)) #Akkor kapunk True értéket, ha a kettő halmaznak nincsenek ugyanolyan értékei, máskülönben False értéket kapunk.

#8
A={1,2,3}
B={1,2,3,4,5}
print(A.issubset(B))
#Az issubset metódussal True értéket kapunk, ha a vizsgált A halmaz elemei  megtalálhatóak a B halmazban, máskülönben False értéket kapunk.

#9
