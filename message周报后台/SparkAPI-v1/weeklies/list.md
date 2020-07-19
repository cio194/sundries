### list

GET `/api/weeklies/`

返回周报列表页，以添加时间排序

---

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter    | Description                                    |
| :----------- | :--------------------------------------------- |
| `p`          | A page number within the paginated result set. |
| `page_size`  | Number of results to return per page.          |
| `author`     |                                                |
| `start_time` |                                                |
| `end_time`   |                                                |
| `search`     | A search term.                                 |

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["weeklies", "list"]
var params = {
    p: ...,
    page_size: ...,
    author: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```