//Deciding to lean some nodeJS after michael reeves stream

let app = require('express')();

app.post('/', (req, res) => {
    console.log("POST request received")
    res.sendStatus(200)
});

app.listen(3000, console.log('server starting on 3000'))