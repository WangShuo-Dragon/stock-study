from dotenv import dotenv_values

class Config:

    def __init__(self, env_path) -> None:
        self.env_value = dotenv_values(env_path)


    def getEnvValue(self, env_key):
        return self.env_value.get(env_key)
        
