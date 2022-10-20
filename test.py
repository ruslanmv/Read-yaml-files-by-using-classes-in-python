from load_yaml import LoadYaml
def one():
    y = LoadYaml()
    y.load_file("test_data.yml")
    print(y.dict())



one()



