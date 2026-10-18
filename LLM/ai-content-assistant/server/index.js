import express from "express"
import cors from "cors"
import dotenv from "dotenv"
import generateRoute from "./routes/generate.js"

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/',(req,res)=>{
    res.json({
        status:"OK",
        message:"AI Content Assistent API is running"
    });
})

app.use('/api/generate',generateRoute)

const PORT = process.env.PORT || 5000;
app.listen(PORT,()=>console.log(`Server running on port ${PORT}`))