import express from 'express';
import fs from 'fs';
import { spawn } from "child_process";
import open from 'open';

const app = express();

app.set('view engine', 'ejs');

const defaultValues = [
    {
        "length": "150",
        "width": "100",
        "height": "40",
        "count": "3",
        "weight": "400"
    },
    {
        "length": "150",
        "width": "100",
        "height": "40",
        "count": "3",
        "weight": "555555"
    },
    {
        "length": "150",
        "width": "100",
        "height": "40",
        "count": "3",
        "weight": "406666660"
    },
    {
        "length": "150",
        "width": "100",
        "height": "40",
        "count": "3",
        "weight": "400"
    },
]

app.get("/", (req, res) => {
    res.render("index", { defaultValues });
});

app.get("/send", (req, res) => {
    parseAndWrite(req.query);
    res.render("submit")
    runScript();
})

app.get('/download', function(req, res){
    const file = `./example.docx`;
    res.download(file); // Set disposition and send it.
  });

app.listen(3000);
console.log("Listening on localhost:3000")
open('http://localhost:3000');

const parseAndWrite = (query) => {
    const newData = {};

    Object.keys(query).forEach((key) => {
        const match = key.match(/(\D*)(\d*)/); // This regex separates the base name and the index
        const base = match[1];
        const index = match[2];

        if (base && index !== "") { // If base name and index are valid
            if (!newData[index]) { // If this index does not exist in new data, create it
                newData[index] = {};
            }

            newData[index][base] = query[key]; // Add the base name and its value to the new data
        }
    });

    fs.writeFile("data.json", JSON.stringify(newData), (err) => {
        if (err)
            console.log(err);
    });
}


const runScript = () => {
    const handler = (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`${stdout}`);
    }

    // const isWin = process.platform === "win32";
    // if (isWin) {
    //     exec('python main.py', handler);
    // }
    // else exec('python3 main.py', handler);
    const command = process.platform === "win32" ? 'python' : 'python3';
    const pythonProcess = spawn(command, ['main.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(data.toString());
    });
}

