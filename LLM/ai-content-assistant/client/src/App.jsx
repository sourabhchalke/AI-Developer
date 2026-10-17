import { useState } from "react";
import "./App.css";
import FeatureSelector from "./components/FeatureSelector";

function App() {

  const [feature,setFeature]=useState("email");
  console.log(feature);
  return (
    <>
      <div className="app">
        <header className="app-header">
          <h1>AI Content Assistant</h1>
          <p>Pick a feature, type your text, and let Gemini do the work.</p>
        </header>

        <FeatureSelector value={feature} onChange={setFeature}/>

      </div>
    </>
  );
}

export default App;
