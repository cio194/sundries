### create

POST `/api/codes/`

发送一个6位短信验证码

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter            | Description |
| :------------------- | :---------- |
| `phone` **required** | 手机号码    |

---

**说明：验证码过期时间为2分钟**

**错误信息**：

```
手机号码格式错误 {"phone": ["手机号码非法"]} 
发送失败 {"phone": "请求参数格式错误"} (注：尚未申请发短信服务)
```

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["codes", "create"]
var params = {
    phone: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```