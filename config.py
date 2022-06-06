from dataclasses import dataclass
from configparser import ConfigParser

@dataclass
class Bot:
    token : str
    adminid : int

@dataclass
class Config:
    TgBot : Bot

def config(path):
    config = ConfigParser()
    config.read(path)
    TgBot = config["tgbot"]
    return Config(
        TgBot=Bot(
            token=TgBot["token"],
            adminid=TgBot["adminid"]
        )
    )