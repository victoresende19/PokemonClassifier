from pydantic import BaseModel


class ModelInput(BaseModel):
    nome_modelo: str
    criterion: str
    max_features: str
    test_train_size: float

    class Config:
        schema_extra = {
            "example": {
                "nome_modelo": "RandomForestClassifierV1",
                "criterion": "entropy",
                "max_features": "sqrt",
                "test_train_size": 0.8
            }
        }


class PredictInput(BaseModel):
    HP: float
    Att: float
    Spd: float
    Def: float
    Height: float
    Weight: float
    nome_modelo: str

    class Config:
        schema_extra = {
            "example": {
                "HP": 0.2,
                "Att": 0.2,
                "Spd": 0.2,
                "Def": 0.2,
                "Height": 0.2,
                "Weight": 0.2,
                "nome_modelo": "random_forest_pokemon"
            }
        }
