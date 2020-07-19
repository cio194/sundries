### read

GET `/api/groups/{id}/`

返回某一个组的详细信息

---

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                 |
| :---------------- | :------------------------------------------ |
| `id` **required** | A unique integer value identifying this 组. |

---

**说明：**
	组内成员返回格式：

```
"groupmembers": [
        {
            "id": 1,
            "name": "admin",
            "occupation": null
        }，
        {...}
    ]
```

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["groups", "read"]
var params = {
    id: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```