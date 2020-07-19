# API说明

----

## 各个模块作用

*applications*：管理员所要处理的申请

*codes*：注册时在此页面生成验证码

*forget*：找回密码页面

*groups*：各个小组

*login*：登录页面，成功生成一个json web token

*projects*：团体项目

*users*：用户

*weeklies*：周报

----

## 权限方面

**要点**： 根据用户的*is_staff*属性判断是否为管理员；
			根据用户的*is_admitted*属性判断是否为正式成员；
			除开登录和找回密码页面，其他页面都需要登录，有的还需要*管理员权限*。



### 管理员权限：

* 查看信息时可看到密码
* 可在用户管理页面中处理申请
* 可在用户管理页面中删除成员
* 可对成员周报进行评论

### 正式成员：

* 基本周报功能

### 非正式成员：

* 啥都不能干



### 权限相关错误信息：

```
未登录：
HTTP 403 Forbidden
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "身份认证信息未提供。"
}
```

```
已登录的非正式成员：
HTTP 403 Forbidden
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "管理员还未同意您的申请"
}
```

``` 
某操作无权限执行(如删除用户或别人的周报等)：
HTTP 403 Forbidden
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "detail": "您没有执行该操作的权限。"
}
```



---

## 其他说明

有关返回的code状态码，我不太清楚是什么格式，页面中是这样：

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {...}
}
```

---

* 后面参数表中ml指代max_length；
* 字符参数空参传入请传"", 而非null
* 有关具体的过滤，排序，搜索用法，最好还是访问aip接口更好