### update

PUT `/api/projects/{id}/`

更新某一项目（只能更新自己创建的项目）

---

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description                                   |
| :---------------- | :-------------------------------------------- |
| `id` **required** | A unique integer value identifying this 项目. |

---

#### Query Parameters

The following parameters should be included as part of a URL query string.

| Parameter    | Description    |
| :----------- | :------------- |
| `start_time` |                |
| `end_time`   |                |
| `search`     | A search term. |

---

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter                    | Description                                                  |
| :--------------------------- | :----------------------------------------------------------- |
| `projectmembers`**required** | 组内成员.嵌套字段，允许多个，字段有三个：name, occupation, task. 都是字符类型，仅name为required |
| `name` **required**          | 名称                                                         |
| `project_type`               | 项目类型                                                     |
| `group_leader`               | 负责人                                                       |
| `describe`                   | 项目描述                                                     |

---

说明和错误与create类似

---

```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["projects", "update"]
var params = {
    id: ...,
    projectmembers: ...,
    name: ...,
    project_type: ...,
    group_leader: ...,
    describe: ...,
    start_time: ...,
    end_time: ...,
    search: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```