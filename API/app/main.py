# FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Functions
from utils.etl import etl_process
from utils.modeling import modeling, predict
from .schema import ModelInput, PredictInput
from traceback import print_exception

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.post("/pokemon/treino/")
async def treino(model_request: ModelInput):

    try:
        # Recebe as variáveis
        nome_modelo = model_request.nome_modelo
        criterion = model_request.criterion
        max_features = model_request.max_features
        test_train_size = model_request.test_train_size

        # Chama função de preprocessamento de dados
        df = etl_process()

        # Chama a função de treino do modelo Random Forest
        accuracy = modeling(
            df=df,
            nome_modelo=nome_modelo,
            criterion=criterion,
            max_features=max_features,
            test_train_size=test_train_size
        )

        return JSONResponse(
            status_code=200,
            content={'acurácia': accuracy},
        )

    except Exception as e:
        print_exception(e)
        return JSONResponse(
            content={'message': 'Internal server error'}, 
            status_code=500
        )


@app.post("/pokemon/previsao/")
async def previsao(predict_request: PredictInput):
    try:
        # ['HP', 'Att', 'Spd', 'Def', 'Height', 'Weight']
        # Recebe as variáveis
        HP = int(predict_request.HP)
        Att = int(predict_request.Att)
        Def = int(predict_request.Def)
        Spd = int(predict_request.Spd)
        Height = int(predict_request.Height)
        Weight = int(predict_request.Weight)
        nome_modelo = predict_request.nome_modelo

        # Chama função de previsão
        predict_new = predict(
            HP=HP,
            Att=Att,
            Def=Def,
            Spd=Spd,
            Height=Height,
            Weight=Weight,
            nome_modelo=nome_modelo
        )

        return JSONResponse(
            status_code=200,
            content={'predição': predict_new[0]},
        )

    except Exception as e:
        print_exception(e)
        return JSONResponse(
            content={'message': 'Internal server error'},
            status_code=500
        )
