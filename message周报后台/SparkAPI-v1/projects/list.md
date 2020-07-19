### list

GET `/api/projects/`

返回团队项目列表页，以添加时间排序

---

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter    | Description                                    |
| :----------- | :--------------------------------------------- |
| `p`          | A page number within the paginated result set. |
| `page_size`  | Number of results to return per page.          |
| `start_time` |                                                |
| `end_time`   |                                                |
| `search`     | A search term.                                 |

---

**注意：**
	*projectmembers*返回格式：

```
"projectmembers": [
                {
                    "id": 1,
                    "name": "lalalawfafawf",
                    "occupation": null,
                    "task": null,
                    "add_time": "2019-09-16T09:31:00",
                    "project": 1
                },
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
var action = ["projects", "list"]
var params = {
    p: ...,
    page_size: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```