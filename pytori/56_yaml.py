import yaml

with open(".github/workflows/pr-check.yml", "r") as file:
    print(yaml.safe_load(file))