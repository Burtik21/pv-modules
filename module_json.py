import json

# Parsování JSON textu do Python slovníku
data = '{"name": "Alice", "age": 23}'
parsed_data = json.loads(data)
print(parsed_data)

# Zápis Python slovníku jako JSON
with open('data.json', 'w') as file:
    json.dump(parsed_data, file)
