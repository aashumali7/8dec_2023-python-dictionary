students = {
    "s1":{"name":"Aashish","surname":"Mali","address":"Neemuch"},
    "s2":{"name":"Aashu","surname":"Mali","address":"mumbai"},
}



for student in students:
    print(f'hello {students[student]["name"]} {students[student]["surname"]} from {students[student]["address"]}')
