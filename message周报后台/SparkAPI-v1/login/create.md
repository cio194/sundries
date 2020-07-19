### create

POST `/api/login/`

该页面返回json web token

----

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter               | Description |
| :---------------------- | :---------- |
| `username` **required** | 用户名      |
| `password` **required** | 密码        |

---

**说明：jwt过期时间为14天**

**错误信息**：

` 未找到自定义方法，错误后直接报用户名或密码错误吧。。。 `

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["login", "create"]
var params = {
    username: ...,
    password: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```