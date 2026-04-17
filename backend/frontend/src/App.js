import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const uploadFile = async () => {
    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append("resume", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🚀 AI Resume Analyzer</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br /><br />

      <button onClick={uploadFile}>Analyze Resume</button>

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Score: {result.score}%</h2>
          <p><strong>Skills Found:</strong> {result.skills_found.join(", ")}</p>
          <p><strong>Missing Skills:</strong> {result.missing_skills.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
