
import './App.css'

function App() {
 

  return (
    <>
      <main className='container'>
        <h1>AI Text Generator</h1>
        <p>Enter a prompt and let AI generate text for you.</p>

        <form>
          <textarea placeholder='Expalin LLMs in simple words'/>
          <button>
            Generate
          </button>
        </form>

      </main>
    </>
  )
}

export default App
