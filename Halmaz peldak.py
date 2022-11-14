reggeli = {'tea', 'vaj', 'piritós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True]) 
print(ebed)
reggeli.add("lekvár")
reggeli.pop()
# reggeli.remove("sajt")
reggeli.discard("sajt")
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}
# metszet
print(reggeli & ebed)
# unio
print(reggeli | ebed)
 # különbség
print(reggeli - ebed)
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)


##szotar##

raktar= {}
print(raktar)
diak= {
    "vezeteknev": "Kiss" , 
    "keresztnev": "Péter" ,
    "eletkor" : 17,
    'menza' : True
}
print(diak['eletkor'])
print(diak.get('eletkor'))
print(diak.get('kollegista', 'nem'))
print('keresztnev' in diak)
diak['eletkor'] = 21
print(diak['eletkor'])
diak['osztaly'] = '10.A'
del diak['vezeteknev']