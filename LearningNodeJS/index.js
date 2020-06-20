
let app = require('express')();

app.post('/doOneThing', (req, res) => {
    console.log('POST request received')
    console.log('Doing One Thing')
    console.log(req)
    res.sendStatus(200)
});

app.post('/doSomeOtherThing', (req, res) => {
    console.log('POST request received')
    console.log('Doing Some Other Thing')
    res.sendStatus(200)
});

app.listen(3000, console.log('server starting on 3000'))