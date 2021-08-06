import yaml
from importlib_resources import files
import os

def load_grow(config_folder="ceaos.resources.config.recipes",
              config_file="config_lettuce_grow.yml"):
    config = files(config_folder).joinpath(config_file).read_text()
    try:
        dictionary = yaml.safe_load(config)
    except yaml.YAMLError as e:
        print(e)
        quit()

    for stage in dictionary.get("stage_ordering"):
        for stages in stage:
            if stage.get('order') == 1:
                stage1 = stage.get('name')
            elif stage.get('order') == 2:
                stage2 = stage.get('name')
            else:
                stage3 = stage.get('name')

    recipe_stages = dict()
    for stages in dictionary.get('stages'):
        if stages.get('name') == stage1:
            recipe1 = stages
            recipe_stages["stage1"] = recipe1
            print(recipe1)
        elif stages.get('name') == stage2:
            recipe2 = stages
            recipe_stages["stage2"] = recipe2
            print(recipe2)
        else:
            recipe3 = stages
            recipe_stages["stage3"] = recipe3

    return recipe_stages

if __name__ == "__main__":
    load_grow()