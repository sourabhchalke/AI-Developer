const InputBox = ({ value, onChange }) => {
  return (
    <div className="input-box">
      <label htmlFor="">Enter your text </label>
      <textarea
        rows={6}
        placeholder="Type or Paste your text here..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      <small>/ 8000 characters</small>
    </div>
  );
};

export default InputBox;
