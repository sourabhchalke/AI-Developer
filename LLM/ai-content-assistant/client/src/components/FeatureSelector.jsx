const FeatureSelector = ({value,onChange}) => {
  const features = [
    { key: "email", label: "Generate Email" },
    { key: "summarize", label: "Summarize Text" },
    { key: "rewrite", label: "Rewrite Text" },
    { key: "job_description", label: "Job Description" },
    { key: "interview_question", label: "Interview Questions" },
  ];

  return (
    <div className="feature-selector">
      {features.map((f) => (
        <button 
            key={f.key}
            className={`feature-btn ${value === f.key ? "active" :""}`}
            onClick={()=>onChange(f.key)}
        >{f.label}</button>
      ))}
    </div>
  );
};

export default FeatureSelector;
