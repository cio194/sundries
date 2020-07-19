### create

POST `/api/weeklies/`

创建周报

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter           | Description                                                  | type                                 |
| :------------------ | :----------------------------------------------------------- | ------------------------------------ |
| `weeklyprojects`    | 周报内项目.嵌套字段，允许多个，字段有五个：name名称, project_type类型, time_plan项目周期, describe项目描述, status项目状态. 都是字符类型，仅name为required | 均为str，ml依次为60, 20, 20, 500, 20 |
| `name` **required** | 姓名                                                         | str(ml=20)                           |
| `occupation`        | 职位                                                         | str(ml=20)                           |
| `group_leader`      | 组长                                                         | str(ml=20)                           |
| `plan`              | 任务计划                                                     | str(ml=1000)                         |
| `completed`         | 是否完成                                                     | str(ml=10)                           |

---

**错误信息(忽略普通长度错误)**

```
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "weeklyprojects": [
        (有两个项目为输入名称){"name": ["请输入项目名称" ]},
                           {"name": ["请输入项目名称"]}
    ],
    "name": [
        "请输入姓名"
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
var action = ["weeklies", "create"]
var params = {
    weeklyprojects: ...,
    name: ...,
    occupation: ...,
    group_leader: ...,
    plan: ...,
    completed: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```