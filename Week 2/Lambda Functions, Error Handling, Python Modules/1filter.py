#writing a lambda function that returns true for every number greater than 10
li= [1,23,4,6,21,33,123,3]

variable= filter(lambda a: a>10,li )
print(list(variable))

