import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
e = '{"name": "John", "age": 30}'

cjson = json.dumps(d)
print(cjson)

#dumps() dump string, pretvara list,dict,tuple u json string

#loads() prima string i vraca dict
data = json.loads(e)
print(data)

#dump() Zapisuje Python objekt direktno u file u JSON formatu.
with open("data.txt", "w") as f:
    json.dump(data, f, indent=4)

with open("data.txt", "r") as fcb:
    data = json.load(fcb)

print(data)
