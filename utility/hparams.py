import json

config_path = "./env/prod.json"


def create_hparams_to_file(config_path, config_data):
    with open(config_path, "w") as f:
        json.dump(config_data, f, indent=2)


def get_hparams_from_file(config_path, as_dict=False):
    with open(config_path, "r") as f:
        data = f.read()
    config = json.loads(data)

    if as_dict:
        return config

    hparams = HParams(**config)
    return hparams


class HParams():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if type(v) == dict:
                v = HParams(**v)
            self[k] = v
        
    def keys(self):
        return self.__dict__.keys()

    def items(self):
        return self.__dict__.items()

    def values(self):
        return self.__dict__.values()

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __contains__(self, key):
        return key in self.__dict__

    def __repr__(self):
        return self.__dict__.__repr__()
