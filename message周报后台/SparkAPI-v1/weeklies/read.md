### read

GET `/api/weeklies/{id}/`

返回某一周报的详细信息

---

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                   |
| :---------------- | :-------------------------------------------- |
| `id` **required** | A unique integer value identifying this 周报. |

---

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter    | Description    |
| :----------- | :------------- |
| `author`     |                |
| `start_time` |                |
| `end_time`   |                |
| `search`     | A search term. |

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["weeklies", "read"]
var params = {
    id: ...,
    author: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```