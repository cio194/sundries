### partial_update

PATCH `/api/applications/{id}/`

接受resp，之后删除相应申请，并对相关user进行处理（删除或者修改is_admitted字段，put和patch效果相同)

----

#### Path Parameters

The following parameters should be included in the URL path.

| Parameter         | Description |
| :---------------- | :---------- |
| `id` **required** | 申请id      |

----

#### Request Body

The request body should be a `"application/json"` encoded object, containing the following items.

| Parameter | Description                      | type    |
| :-------- | :------------------------------- | ------- |
| `resp`    | 管理员处理申请，0为拒绝，1为同意 | boolean |

----

**注意：申请拒绝后，用户注册信息和申请信息均会被删除**



```
var coreapi = window.coreapi  // Loaded by `coreapi.js`
var schema = window.schema    // Loaded by `schema.js`

// Initialize a client
var client = new coreapi.Client()

// Interact with the API endpoint
var action = ["applications", "partial_update"]
var params = {
    id: ...,
    resp: ...,
}
client.action(schema, action, params).then(function(result) {
    // Return value is in 'result'
})
```