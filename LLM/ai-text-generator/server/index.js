import "dotenv/config"
import express from "express"
import cors from "cors"
import { GoogleGenAI } from "@google/genai"

const app=express();
const PORT = process.env.PORT || 3000;

// Validate configuration before starting
if(!process.env.GEMINI_API_KEY){
    console.error("GEMINI_API_KEY is missing from .env");
    process.exit(1);
}

const ai = new GoogleGenAI({
    apiKey:process.env.GEMINI_API_KEY,
});

app.use(cors({ origin: "http://localhost:5173" }));
app.use(express.json());

// Test whether backend is running
app.get("/api/health",(req,res)=>{
    res.json({status:"Backend is running"});
});


app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});