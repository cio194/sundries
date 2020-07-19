### list

GET `/api/applications/`

返回申请列表页，以添加时间排序

----

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description  |
| :---------- | :----------- |
| `p`         | 第几页       |
| `page_size` | 每页结果条数 |

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["applications", "list"]
var params = {
    p: ...,
    page_size: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```