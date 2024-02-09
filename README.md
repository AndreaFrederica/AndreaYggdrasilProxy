# AndreaYggdrasilProxy
AndreaYggdrasilProxy/YggrasilAndreaProxy（AYP/YAP）

#### 介绍
yggdrasil-proxy的一个简单Python实现  
可以实现多服务器验证  
替代老旧的YggdrasilOfficalProxy  
有什么需要可以直接发邮件催我 看得到的话我会第一时间回复  
Email: andreafrederica@outlook.com

#### 软件架构
整个项目采用FastAPI搓的  
依赖管理采用pipenv  
launcher为启动器  
main为主程序（主要业务逻辑）
Config.py只保存编码格式 请注意  
别的乱七八糟的模块全在module里面 复用的老WSIO框架代码

#### 如何使用

*基于默认配置文件的*
```
-javaagent:authlib-injector-1.2.3.jar=http://127.0.0.1:32217

```


#### 安装教程

##### 源码安装
1.  安装Python3.10版本
2.  安装pipenv
3.  在终端执行 ``pipenv install``
4.  ``pipenv run launcher.py``
5.  补全配置文件
6.  回到第四步 enjoy it

##### 安装二进制版本
1.  从Release下载二进制版本
2.  运行
3.  补全配置文件
4.  回到第二步 enjoy it

##### 构建二进制版本(Windows)
0.  此方案采用 *Nuitka* 构建
1.  安装Python3.10版本
2.  安装pipenv
3.  在终端执行 ``pipenv install``
4.  ``pipenv shell``
5.  ``./build.ps1``
6.  Wait a moment（请确认网络良好 并且补全编译环境）
7.  于 *Build* 目录中找到构建产物

##### 构建二进制版本(Linux)
1.  安装 *pwsh*
2.  同Windows构建方式

#### 使用说明

1.  修改配置文件
    *配置文件范例*
    
    ```json5
    {
        //* AndreaYggdrasilProxy
        //! YAP/AYP 目前不计划支持Https功能 请使用 Nginx 添加Https支持
        //! YAP/APY 使用Json5格式的配置文件

        //? 启用代理服务
        Enable : true,
        //? 保存Log到Log文件中
        Log: false,
        //? 监听的IP
        IP : "0.0.0.0",
        // ? 监听的端口
        Port : 32217,
        YggdrasilServers : [
            {
                //! Mojang 官方验证服务器 受代理的
                //? 一般来说官方服务器优先级最高 但是你可以不用官方验证服务器 直接注释掉即可
                Level : 0,
                Name: "Mojang_Proxied",
                //! 服务器等级 越小优先级越高
                Url : "https://sessionserver.mojang.com",
                //? 可以独立为某个服务器配置代理服务 建议使用Http代理
                    Proxies : {
                    'http': 'http://127.0.0.1:7890',
                    'https': 'http://127.0.0.1:7890'
                }
            },
            {
                //! LittleSkin
                //? Blessing Skin Server 标准 Yggdrasil 配置规范
                Level : 1,
                Name: "LittleSkin",
                //! 注意这个URL格式! 和大部分皮肤站提供的不太一样
                //? 多了    /sessionserver  一截
                Url : "https://littleskin.cn/api/yggdrasil/sessionserver",
                //? ProfileAPI 支持尚未全部完成 目前为可选字段 不配置该字段YAP会自动推断
                ProfileAPI : "https://littleskin.cn/api/profiles/minecraft"
            },
                    {
                //! Mojang 官方验证服务器
                Level : 99,
                Name: "Mojang",
                Url : "https://sessionserver.mojang.com",
            },
        ]
    }

    ```


#### 参与贡献

##### 待办事项
1.  帮忙写英文文档 Tanks. 一直咕咕咕懒得写（跑）
2.  ~~帮忙写编译脚本打包二进制（跑）~~
3.  联系方式 andreafrederica@outlook.com 打包完二进制什么的可以联系我（跑）

##### 流程
1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
5.  发邮件催我

