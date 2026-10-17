import { useState } from "react";
import "./App.css";
import FeatureSelector from "./components/FeatureSelector";
import InputBox from "./components/InputBox";

function App() {

  const [feature,setFeature]=useState("email");
  console.log(feature);
  const [input,setInput]=useState("");
  return (
    <>
      <div className="app">
        <header className="app-header">
          <h1>AI Content Assistant</h1>
          <p>Pick a feature, type your text, and let Gemini do the work.</p>
        </header>

        <FeatureSelector value={feature} onChange={setFeature}/>

        <InputBox value={input} onChange={setInput}/>

      </div>
    </>
  );
}

export default App;
