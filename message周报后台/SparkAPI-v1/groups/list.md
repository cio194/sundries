### list

GET `/api/groups/`

返回组的列表页

----

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["groups", "list"]
client.action(schema, action).then(function(result) {
    // Return value is in 'result'
})
```