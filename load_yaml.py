"""
A quick Singleton module for reading yaml. This will make is quick and easy
to load and use settings files throughout a program
"""
import sys
import os
import importlib.util



class Input:
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data

        
class LoadYaml(Input):
    """This class now shares all its attributes among its various instances"""

    def __init__(self, **kwargs):
        Input.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)

    def get(self, name, default=None):
        """ return value for key if it exists, if not return default """
        return self._shared_data.get(name, default)

    def set(self, name, value):
        """ set value for key. If key does not exist, a new dict entry will be created """
        self._shared_data[name] = value

    def dict(self):
        """ return dictionary of global settings"""
        return self.__dict__


    def load_file(self, path):
        ext = os.path.splitext(path)[1][1:]
        if ext == 'yml' or ext == 'yaml':
            self._read_yaml_file(path)
        else:
            print("input file extension must be yml, yaml")


    def _read_yaml_file(self, path):
        """ read in a yaml text file and populate Singleton's dict with entries.
        """
        name = 'yaml'
        spec = importlib.util.find_spec(name)
        if spec is not None:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules[name] = module
            import yaml

            try:
                read_file = open(path, 'r')
                ldata = yaml.load(read_file, Loader=yaml.SafeLoader)

            except IOError as e:
                err = "I/O error({0}): {1} {2}".format(e.errno, e.strerror, path)
                print(err)

            except yaml.YAMLError as e:
                err = "Error in configuration file: {}".format(e)
                print(err)

            else:
                self._shared_data.update(ldata)
        else:
            print("PyYaml module not found. Unable to read yaml file")
