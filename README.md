# How to read  configuration files in Yaml format by using classes in python



Today we are going to create a class in python that will allow us read configuration files in Yaml .

This program aim to help read yaml files in an easy way.

**readyaml** provides a class that provides a dictionary for keeping items that will be available globally.
Yaml can also be parsed and added to the dictionary.  This is useful for reading config files. 

# How to use

First we need to load this class

```python
from load_yaml import LoadYaml
```



## Example 1

Let us assume that you have  this yaml file called **test_data.yml**

```yaml
APP:
  ENVIRONMENT: test
  DEBUG: True
  # Only accept True or False

DATABASE:
  USERNAME: ruslanmv
  PASSWORD: abcd
  HOST: 127.0.0.1
  PORT: 5432
  DB: capgeminidb
```



Then we can define the file

```python
y = LoadYaml()
y.load_file("test_data.yml")
```

```python
print(y.dict())
```

you will get

```json
{'APP': {'ENVIRONMENT': 'test', 'DEBUG': True}, 'DATABASE': {'USERNAME': 'ruslanmv', 'PASSWORD': 'abcd', 'HOST': '127.0.0.1', 'PORT': 5432, 'DB': 'capgeminidb'}}
```

## Example 2

We can create a singleton object and add our first acronym

```python
x = LoadYaml(USERNAME="Nicola")
```

Print the object

```
print(x)
```

```json
{'USERNAME': 'Nicola'}
```

Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym.

```python
z = LoadYaml(DB="leapaudit")
```

 Print the object

```
print(z)
```

```
{'DB': 'leapaudit'}
```

