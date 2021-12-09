import yaml


class YamlHelper:
    @staticmethod
    def read_yaml(yaml_file_path):
        with open(yaml_file_path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)