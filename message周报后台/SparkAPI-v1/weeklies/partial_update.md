### partial_update

PATCH `/api/weeklies/{id}/`

更新评论（当用户为管理员时才能进行此操作，且管理员无法评论自己的周报，普通用户无法使用patch）

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

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter | Description | type        |
| :-------- | :---------- | ----------- |
| `comment` | 评论        | str(ml=150) |

---

**错误信息**

```
HTTP 400 Bad Request
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "comment": [
        "请填写评论"
    ]
}
```

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["weeklies", "partial_update"]
var params = {
    id: ...,
    comment: ...,
    author: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```