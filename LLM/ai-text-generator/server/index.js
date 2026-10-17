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


// Generate AI Text
app.post("/api/generate",async (req,res)=>{
    try {
        const {prompt}=req.body ?? {};

        if(typeof prompt !== "string" || !prompt.trim()){
            return res.status(400).json({
                error:"Please enter a prompt.",
            });
        }

        if(prompt.length > 4000){
            return res.status(400).json({
                error:"Prompt must be 4000 characters or fewer.",
            });
        }

        const response=await ai.models.generateContent({
            model:"gemini-3.8-flash",
            contents:prompt.trim(),
        });

        const text=response.text;

        if(!text){
            return res.status(502).json({
                error:"The AI returned no text. Please try again.",
            });
        }

        return res.json({text})


    } catch (error) {
        // Keep detailed diagnostics on the server
        console.error("Gemini API error :", error.message);

        return res.status(502).json({
            error:"AI generation failed. Check your API access and try again.",
        });

    }
});


app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});