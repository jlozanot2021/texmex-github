import io

with io.open('recetas.md','r') as file:
    print(file.read())
