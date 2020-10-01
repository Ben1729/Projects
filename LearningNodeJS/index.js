
let app = require('express')();

app.get('/doOneThing', (req, res) => {
    console.log('POST request received')
    console.log('Doing One Thing')
    console.log(req)
    res.send('<h1>stuff and things<h1/>')
    res.sendStatus(200)
});

app.get('/doSomeOtherThing', (req, res) => {
    console.log('POST request received')
    console.log('Doing Some Other Thing')
    res.sendStatus(200)
});

app.listen(3000, console.log('server starting on 3000'))