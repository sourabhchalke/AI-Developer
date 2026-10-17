import { useState } from "react";
import "./App.css";
import FeatureSelector from "./components/FeatureSelector";
import InputBox from "./components/InputBox";
import OutputBox from "./components/OutputBox";

function App() {

  const [feature,setFeature]=useState("email");
  console.log(feature);
  const [input,setInput]=useState("");
  console.log(input);
  const [output,setOutput]=useState("");
  console.log(output);
  const [loading,setLoading]=useState(false);
  return (
    <>
      <div className="app">
        <header className="app-header">
          <h1>AI Content Assistant</h1>
          <p>Pick a feature, type your text, and let Gemini do the work.</p>
        </header>

        <FeatureSelector value={feature} onChange={setFeature}/>

        <InputBox value={input} onChange={setInput}/>

        <OutputBox output={output} loading={loading} />

      </div>
    </>
  );
}

export default App;
