### read

GET `/api/users/{id}/`

返回某一用户详细信息

---

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                   |
| :---------------- | :-------------------------------------------- |
| `id` **required** | A unique integer value identifying this 用户. |

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["users", "read"]
var params = {
    id: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```