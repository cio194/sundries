### update

PUT `/api/weeklies/{id}/` 

更新某一周报信息（仅能更新自己的周报）

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

| Parameter           | Description                                                  |
| :------------------ | :----------------------------------------------------------- |
| `weeklyprojects`    | 周报内项目.嵌套字段，允许多个，字段有五个：name, project_type, time_plan, describe, status. 都是字符类型，仅name为required |
| `name` **required** | 姓名                                                         |
| `occupation`        | 职位                                                         |
| `group_leader`      | 组长                                                         |
| `plan`              | 任务计划                                                     |
| `completed`         | 是否完成                                                     |

---

错误与create类似

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["weeklies", "update"]
var params = {
    id: ...,
    weeklyprojects: ...,
    name: ...,
    occupation: ...,
    group_leader: ...,
    plan: ...,
    completed: ...,
    author: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```