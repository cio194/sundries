### partial_update

PATCH `/api/users/{id}/`

更新用户个人信息（仅能更新自己的信息）(put和patch效果相同)

---

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                   |
| :---------------- | :-------------------------------------------- |
| `id` **required** | A unique integer value identifying this 用户. |

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter    | Description | type                                         |
| :----------- | :---------- | -------------------------------------------- |
| `name`       | 真实姓名    | str(ml=20)                                   |
| `stu_id`     | 学号        | str(ml=15)                                   |
| `email`      | 邮箱        | str(ml=100)                                  |
| `address`    | 地址        | str(ml=100)                                  |
| `occupation` | 职位        | 为枚举(choice)类型，值为整数，展示值为字符串 |

---

**说明：**
occupation：
OCCUPATION_TYPE = (        (1, "前端"), (2, "后台"), (3, "运维"), (4, "UI"), (5, "产品经理"), (6, "其他")    )
此为枚举类型，希望在填此项时给一个选项，值由1～6依次对应

**错误信息**(忽略普通长度错误)

```
{
    "name": [
        "请输入真实姓名"
    ],
    "email": [
        "请输入合法的邮件地址。"
    ],
    "occupation": [
        "xxx不是合法选项。"
    ]
}
```



----

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["users", "partial_update"]
var params = {
    id: ...,
    name: ...,
    stu_id: ...,
    email: ...,
    address: ...,
    occupation: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```