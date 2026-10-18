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

router.post('/',async(req,res)=>{
    res.json({status:"OK",message:"Generate Route working"});
})

export default router;