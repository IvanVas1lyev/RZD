import express from 'express';
import fs from 'fs';
import { spawn } from "child_process";
import open from 'open';
import { defaultValues } from './defaultValues.js';

const app = express();

app.set('view engine', 'ejs');
app.use('/public', express.static('public'));



app.get("/", (req, res) => {
    res.render("index");
});

app.get("/send", (req, res) => {
    parseAndWrite(req.query);
    res.render("submit")
    runScript();
})

app.get('/download', function (req, res) {
    const file = `./Расчетно-пояснительная записка.docx`;
    res.download(file); // Set disposition and send it.
});

app.get('/render-forms', (req, res) => {
    const numForms = req.query.count;
    res.render('forms', { numForms, defaultValues });
});

app.listen(3000);
console.log("Listening on localhost:3000")
open('http://localhost:3000');

const parseAndWrite = (query) => {
    const newData = { name: query.name, cargoCount: query.cargoCount };

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
    const command = process.platform === "win32" ? 'python' : 'python3';
    const pythonProcess = spawn(command, ['main.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(data.toString());
    });
}