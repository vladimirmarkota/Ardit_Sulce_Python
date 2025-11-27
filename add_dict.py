from pprint import pprint

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#d["employees"].append({"firstName": "Vladimir", "lastName": "Markota"})
pprint(d["employees"])
d["employees"].append(dict(firstName = "Vanja", lastName = "Bertovic"))
pprint(d["employees"])
