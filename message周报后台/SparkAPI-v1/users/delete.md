### delete

DELETE `/api/users/{id}/`

删除某一用户（仅管理员能删除用户，且管理员不能删除自己）

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
var action = ["users", "delete"]
var params = {
    id: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```