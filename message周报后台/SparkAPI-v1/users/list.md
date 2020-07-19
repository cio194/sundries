### list

GET `/api/users/`

返回用户列表页，以加入时间排序

---

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter   | Description                                    |
| :---------- | :--------------------------------------------- |
| `p`         | A page number within the paginated result set. |
| `page_size` | Number of results to return per page.          |

---

**说明：不为管理员时，password_unencoded字段显示如下**(read一样)

```
"password_unencoded": "仅管理员可见"
```

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["users", "list"]
var params = {
    p: ...,
    page_size: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```