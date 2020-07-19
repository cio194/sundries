### create

POST `/api/projects/`

创建团队项目

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                    | Description                                                  | type                         |
| :--------------------------- | :----------------------------------------------------------- | ---------------------------- |
| `projectmembers`**required** | 项目成员.嵌套字段，允许多个，字段有三个：name姓名, occupation职位, task任务. 都是字符类型，仅name为required | 均为str, ml依次为20, 20, 100 |
| `name` **required**          | 名称                                                         | str(ml=100)                  |
| `project_type`               | 项目类型                                                     | str(ml=20)                   |
| `group_leader`               | 负责人                                                       | str(ml=20)                   |
| `describe`                   | 项目描述                                                     | str(ml=1000)                 |

---

**说明：**
	*projectmembers*传入格式：

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

**错误信息(普通长度错误未包含)：**

```
{
    "projectmembers": [
        (此字段为空)"至少需要一位成员",
        (有两个成员姓名过长){"name": ["长度不能超过20个字符"]},
                         {"name": ["长度不能超过20个字符"]}
    ],
    "name": [
        "请输入名称"
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
var action = ["projects", "create"]
var params = {
    projectmembers: ...,
    name: ...,
    project_type: ...,
    group_leader: ...,
    describe: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```