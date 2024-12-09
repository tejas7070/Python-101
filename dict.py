dict = {
    
    "name": ["John","Tejas"],
    "marks" :{
        "maths": 90,
        "science": 85
        },

"Age":  [21,22],
"Gender": ["Male","Female"]
}
print(dict["marks"]["maths"])
print(dict["Age"])
print(dict["name"])
print(dict["Gender"])
print(dict.update({ "money":100} ))
print(dict.items())
print(list(dict.keys()))
print(list(dict.values()))