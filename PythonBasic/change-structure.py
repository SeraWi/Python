#자료 구조의 변형
menu ={"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

menu =list(menu)
print(menu, type(menu)) #['커피', '우유', '주스'] <class 'list'>

menu =tuple(menu)
print(menu, type(menu)) #('커피', '우유', '주스') <class 'tuple'>

menu=set(menu)
print(menu,type(menu)) #{'커피', '우유', '주스'} <class 'set'>

