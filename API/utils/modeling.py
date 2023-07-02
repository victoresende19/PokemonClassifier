# Modelagem
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import pickle

# Balanceamento de classes
from imblearn.over_sampling import SMOTE

# Manipulacao dados
import numpy as np
import pandas as pd
from pandas import DataFrame

# Visualizacao
import matplotlib.pyplot as plt


def modeling(df: DataFrame, criterion, max_features, test_train_size, nome_modelo):
    
    # Seleção das variáveis
    cols = ['HP', 'Att', 'Spd', 'Def', 'Height', 'Weight']
    X = df.loc[:, cols].values
    y = df.loc[:, 'Type 1'].values

    # Treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_train_size, stratify=y)


    # Random forest
    rf = RandomForestClassifier(
        random_state=49, bootstrap=True, criterion=criterion, max_features=max_features)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    # Salvando o modelo
    with open(f"models/{nome_modelo}.pkl", "wb") as f:
        pickle.dump(rf, f)

    # Acurácia
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy


def predict(HP, Att, Spd, Def, Height, Weight, nome_modelo):
    # Carregar o modelo
    with open(f"models/{nome_modelo}.pkl", "rb") as f:
        modelo_carregado = pickle.load(f)

    value = np.array([HP, Att, Spd, Def, Height, Weight]).reshape(-1, 6)
    return modelo_carregado.predict(value).tolist()




    
