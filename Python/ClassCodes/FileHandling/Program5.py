import pickle

fobj = open("file1.pkl", "wb+")

player = {"name": "Sachin", "age": 45, "country": "India"}

data = [1, 2, 3, 4, 5]

pickle.dump(player, fobj)
pickle.dump(data, fobj)

fobj.seek(0)

obj1 = pickle.load(fobj)
obj2 = pickle.load(fobj)

print(obj1)
print(obj2)

fobj.close()