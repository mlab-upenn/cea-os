import yaml
from importlib_resources import files

def load_config(config_folder="ceaos.resources.config", config_file="config_lettuce_grow.yml"):
    config = files(config_folder).joinpath(config_file).read_text()
    try:
        dictionary = yaml.safe_load(config)
        for key, value in dictionary.items():
            print (key + " : " + str(value))
    except yaml.YAMLError as e:
        print(e)
        quit()

if __name__ == '__main__':
    load_config()
