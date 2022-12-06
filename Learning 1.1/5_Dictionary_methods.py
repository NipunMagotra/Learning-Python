from dbm import ndbm


dic = {
    "Nipun":   "My first name",
    "Magotra": "My second name",
    "list" : [1,2,3],
    "tuple" : (4,),
    "anotherdic":{"Bharatwaj": "My goutra"},
    1:323223
}
print(dic["Nipun"])
print(dic["Magotra"])
dic["list"] = [0,0,0,0]
print(dic["list"])
print(dic["tuple"])
print(dic["anotherdic"]["Bharatwaj"])
print((dic.keys())) #  it return the keys 
print((dic.values())) # it return the values
print((dic.items()))  # prints the items(keys and values)
new_dic = {"roti" : "kapda",
"kapda" : "Mkaan"} 
dic.update(new_dic) #updates the dictionary by key:Value pairs using update function
print(dic.get("Nipun1")) #print value associated with key Nipun
print(dic["Nipun1"]) #print value associated with key Nipun

print(dic.get("Nipun1")) #returns none when the key not present
print(dic["Nipun1"]) # Throws a error when the key is not present

