import pandas

my_dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

my_var = pandas.DataFrame(my_dataset)

print(my_var)