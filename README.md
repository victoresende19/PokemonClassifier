# 🐛 Pokemon Cluster Classifier 🐛
<hr>

![image](https://user-images.githubusercontent.com/63743020/206604130-a80cd71e-7c8c-4174-ae54-20aa8627dec5.png): Criado em FastAPI e React, o projeto cria dois endpoint e uma interface web para a predição do tipo dos Pokémons de acordo com os valores inputados, considerando as 8 primeiras gerações. Dessa forma, a modelagem é feita selecionando as variáveis HP, Ataque, Defesa, Velocidade, Altura, Peso, e de acordo com os valores inputados, a previsão de qual tipo as características inputadas pertencem. 

### Base de dados
Acesse a base de dados aqui: https://www.kaggle.com/datasets/rounakbanik/pokemon.

### Modelagem:
- Pre-processamento necessário
- Seleção das variáveis: HP, Ataque, Defesa, Velocidade, Altura, Peso;
- Padronização: Padroniza as variáveis por serem de escalas diferentes;
- Separação em treino e teste;
- RandomForestClassifier para classificar os pokemons de acordo com as variáveis HP, Ataque, Defesa, Velocidade, Altura, Peso;
- Salva-se o modelo.

### Endpoints (FastAPI):
- /pokemon/treino: Para criação do modelo de acordo como o citado acima. Pode receber as seguintes variáveis:
  - nome_modelo
  - criterion
  - max_features
  - test_train_size

- /pokemon/previsao: Para a predição de acordo com as variáveis abaixo e respectivos dados dos quais serão inputado:
  - HP
  - Att
  - Def
  - Spd
  - Altura
  - Peso
  - nome_modelo

Para iniciar o backend da aplicação, apenas digite o comando abaixo:
- python -m uvicorn app.main:app --reload

### Interface (React):
Para rodar a interface, apenas digite os comando a seguir:
- npm install
- npm start

E então, a seguinte tela aparecerá:
![image](https://github.com/victoresende19/PokemonClassifier/assets/63743020/af0e1dac-b129-4f21-96eb-c93ae0b511f9)

<hr>

![image](https://user-images.githubusercontent.com/63743020/206604148-edc3020b-2ddf-4b9d-aff4-04116150f285.png): Created in FastAPI and React, the project creates two endpoints and a web interface for predicting the type of Pokémon according to the entered values, considering the 8 generations. In this way, modeling is done by selecting the variables HP, Attack, Defense, Speed, Height, Weight, and according to the entered values, the prediction of which type of inserted characteristics they belong to.

### Database
Access the database here: https://www.kaggle.com/datasets/rounakbanik/pokemon.

### Modeling:
- Pre-processing required;
- Selection of variables: HP, Attack, Defense, Speed, Height, Weight;
- Standardization: Standardizes the variables because they are from different scales;
- Separation into training and testing;
- RandomForestClassifier to classify pokemons according to variables HP, Attack, Defense, Speed, Height, Weight;
- The model is saved.

### Endpoints (FastAPI):
- /pokemon/treino: For creating the model as mentioned above. It can receive the following variables:
  - nome_modelo
  - criterion
  - max_features
  - test_train_size

- /pokemon/previsao: For the prediction according to the variables below and respective data which will be inserted:
  - HP
  - Att
  - Def
  - Spd
  - Height
  - Weight
  - nome_modelo

To run the backend, just type the comand below:
- python -m uvicorn app.main:app --reload

### Interface (React)
To run the interface, just type the commands below:
- npm install
- npm start

And then, this window will open:
![image](https://github.com/victoresende19/PokemonClassifier/assets/63743020/af0e1dac-b129-4f21-96eb-c93ae0b511f9)

<hr>
Victor Resende.
