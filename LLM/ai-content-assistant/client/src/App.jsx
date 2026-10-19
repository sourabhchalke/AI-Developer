import { useState } from "react";
import "./App.css";
import FeatureSelector from "./components/FeatureSelector";
import InputBox from "./components/InputBox";
import OutputBox from "./components/OutputBox";

function App() {
  const [feature, setFeature] = useState("email");
  console.log(feature);
  const [input, setInput] = useState("");
  console.log(input);
  const [output, setOutput] = useState("");
  console.log(output);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!input.trim()) {
      setOutput("Please enter some text first.");
      return;
    }

    setLoading(true);
    setOutput("");

    const API_URL = import.meta.env.VITE_API_URL;

    try {
      
      const res = await fetch(`${API_URL}/api/generate`,{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({feature,input}),
      });

      const data = await res.json();
      setOutput(data.error ? "Error!" +data.error : data.output);

    } catch (err) {
      setOutput("Network Error. Is the backend running?");
      console.log(err);
    }finally{
      setLoading(false);
    }


  };

  return (
    <>
      <div className="app">
        <header className="app-header">
          <h1>AI Content Assistant</h1>
          <p>Pick a feature, type your text, and let AI do the work.</p>
        </header>

        <FeatureSelector value={feature} onChange={setFeature} />

        <InputBox value={input} onChange={setInput} />

        <button
          className="generate-btn"
          onClick={handleGenerate}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate"}
        </button>

        <OutputBox output={output} loading={loading} />
      </div>
    </>
  );
}

export default App;
