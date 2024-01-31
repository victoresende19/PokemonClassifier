import React, { useState } from "react";
import axios from "axios";
import "./App.css";
import pokemonLogo from "../src/images/pokemon-logo-8.png";

function App() {
  const [pokemonData, setPokemonData] = useState({
    HP: 0.0,
    Att: 0.0,
    Spd: 0.0,
    Def: 0.0,
    Height: 0.0,
    Weight: 0.0,
    nome_modelo: ""
  });
  const [predictionResult, setPredictionResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event: any) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "https://pokemon-classifier-api.onrender.com/pokemon/previsao/",
        pokemonData
      );
      setPredictionResult(response.data);
      setError(null);
    } catch (error) {
      setPredictionResult(null);
      console.error(error);
    }
  };

  const handleChange = (event: any) => {
    const { name, value } = event.target;
    setPokemonData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  return (
    <div className="App">
      <div className="header">
        <img src={pokemonLogo} alt="Pokémon Logo" className="logo" />
      </div>
      <form onSubmit={handleSubmit}>
        <h4 className="description">
          Preencha os campos abaixo para prever o tipo primário do Pokémon:
        </h4>
        <div className="input-container">
          <div className="column">
            <div className="input-group">
              <label htmlFor="HP">HP:</label>
              <input
                type="number"
                id="HP"
                name="HP"
                placeholder="0.0"
                value={pokemonData.HP}
                onChange={handleChange}
              />
            </div>
            <div className="input-group">
              <label htmlFor="Spd">Velocidade:</label>
              <input
                type="number"
                id="Spd"
                name="Spd"
                placeholder="0.0"
                value={pokemonData.Spd}
                onChange={handleChange}
              />
            </div>
            <div className="input-group">
              <label htmlFor="Height">Altura:</label>
              <input
                type="number"
                id="Height"
                name="Height"
                placeholder="0.0"
                value={pokemonData.Height}
                onChange={handleChange}
              />
            </div>
            <div className="input-group">
              <label htmlFor="Att">Ataque:</label>
              <input
                type="number"
                id="Att"
                name="Att"
                placeholder="0.0"
                value={pokemonData.Att}
                onChange={handleChange}
              />
            </div>
            <div className="input-group">
              <label htmlFor="Def">Defesa:</label>
              <input
                type="number"
                id="Def"
                name="Def"
                placeholder="0.0"
                value={pokemonData.Def}
                onChange={handleChange}
              />
            </div>
            <div className="input-group">
              <label htmlFor="Weight">Peso:</label>
              <input
                type="number"
                id="Weight"
                name="Weight"
                placeholder="0.0"
                value={pokemonData.Weight}
                onChange={handleChange}
              />
            </div>
          </div>
        </div>
        <div className="input-container">
          <label htmlFor="nome_modelo">Nome do Modelo:</label>
          <select
            id="nome_modelo"
            name="nome_modelo"
            value={pokemonData.nome_modelo}
            onChange={handleChange}
          >
            <option value="">Selecione um modelo</option>
            <option value="random_forest_pokemon_v1">
              Modelo 1 - Random forest V1
            </option>
            <option value="random_forest_pokemon_v2">
              Modelo 2 - Random forest V2
            </option>
            <option value="random_forest_pokemon_v3">
              Modelo 3 - Random forest V3
            </option>
          </select>
        </div>
        <button className="submit-button" type="submit">
          Enviar
        </button>
      </form>

      {predictionResult && (
        <div className="prediction-result">
          <h2>O tipo do Pokémon é: {predictionResult["predição"]}</h2>
        </div>
      )}

      {error && <div className="error">{error}</div>}
    </div>
  );

}

export default App;
