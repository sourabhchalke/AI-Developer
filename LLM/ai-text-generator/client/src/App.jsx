import { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoadig] = useState("");

  async function generateText(event) {
    event.preventDefault();

    try {
      const response = await fetch("http://localhost:3000/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Something went wrong.");
      }

      setResult(data.text);
    } catch (error) {
      setError(
        error.message === "Failed to fetch"
          ? "Cannot connect to the backend. Is it running?"
          : error.message,
      );
    } finally {
      setLoadig(false);
    }
  }

  return (
    <>
      <main className="container">
        <h1>AI Text Generator</h1>
        <p>Enter a prompt and let AI generate text for you.</p>

        <form onSubmit={generateText}>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Expalin LLMs in simple words"
            maxLength={4000}
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? "Generating..." : "Generate Text"}
          </button>
        </form>

        {loading && <p>AI is thinking...</p>}
        {error && <p className="error">{error}</p>}

        {result && (
          <section className="result">
            <h2>AI Response</h2>
            <p className="output">{result}</p>
          </section>
        )}

      </main>
    </>
  );
}

export default App;
