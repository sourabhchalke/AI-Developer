import "dotenv/config";
import express from "express";
import { GoogleGenAI } from "@google/genai";

const router = express.Router();
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// One System prompt per feature
const prompts = {
  email:
    "You are a professional email writer. Write a clear, polite email with a subject line. Return only the email.",
  summarize:
    "You are an expert editor. Summarize the text into 3-5 bullet points covering the key ideas.",
  rewrite:
    "You are an editor. Rewrite the text to be clearer and more professional, keeping the same meaning.",
  job_description:
    "You are a technical recruiter. Write a job description with these sections: Role Summary, Responsibilities, Requirements, Nice-to-Haves.",
  interview_question:
    "You are a senior interviewer. Generate 8 interview questions (mix of technical and behavioral). Number them.",
};

router.post("/", async (req, res) => {

  const { feature, input } = req.body;

  // Validation
  if (!prompts[feature]) {
    return res.status(400).json({ error: "Invalid Feature" });
  }
  if (!input) {
    return res.status(400).json({error:"Please enter some text"})
  }
  if(input.length>8000){
    return res.status(400).json({error:"Input too long (max 8000 character)"})
  }

  try {
    
    // Call Gemini
    const response = await ai.models.generateContent({
        model:"gemini-3.8-flash",
        contents:input,
        config:{
            systemInstruction:prompts[feature],
            temperature:0.7,
        },
    });

    res.json({output:response.text});
    

  } catch (error) {
    console.log("Gemini AI error",error.message);
    res.status(500).json({error:"AI Failed. Try Again."});
  }
});

export default router;
