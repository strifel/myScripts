const express = require('express')
var beautify = require('js-beautify').js
const app = express()
const port = 3000

app.get('/*', (req, res) => {
  let json = JSON.stringify({url: req.url, header: req.headers, query: req.query})
  console.log(beautify(json, { indent_size: 2, space_in_empty_paren: true }))
  res.setHeader('Content-Type', 'application/json');
  res.send(json)
})

app.listen(port, () => console.log(`Listening on port ${port}!`))
