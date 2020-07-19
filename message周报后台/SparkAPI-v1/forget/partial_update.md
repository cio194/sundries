### partial_update

PATCH `/api/forget/`

修改密码

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter     | Description | **type** |
| :------------ | :---------- | -------- |
| `phone`       | 手机号码    | str      |
| `code`        | 验证码()    | str      |
| `password`    | 密码        | str      |
| `re_password` | 确认密码    | str      |

----

###错误信息

```
{
    "phone": [
        (格式错误)"手机号码非法",
        (未注册用户)"用户不存在",
        (为空)"请输入手机号码"
    ],
    "code": [
        "验证码错误",
        "验证码格式错误",
        "验证码过期",
        "请输入验证码"
    ],
    "password": [
        "请输入密码",
        "最大不能超过16个字符",
        "最小不能少于8个字符"
    ],
    "re_password": [
        "请重复密码",
        "两次密码不一致"
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
var action = ["forget", "partial_update"]
var params = {
    phone: ...,
    code: ...,
    password: ...,
    re_password: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```

