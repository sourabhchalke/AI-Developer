
const OutputBox = ({output,loading}) => {

    if(loading) return <div className="output-box loading">Generating...</div>
    if(!output) return null;

    const copy=()=> navigator.clipboard.writeText(output);

  return (
    <div className="output-box">
        <div className="output-header">
            <span>AI Response</span>
            <button className="copy-btn" onClick={copy}>Copy</button>
        </div>
        <pre>{output}</pre>
    </div>
  )
}

export default OutputBox
