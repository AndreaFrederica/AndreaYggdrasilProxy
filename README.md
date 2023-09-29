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
        Enable : true,
        Log : false,
        IP : "0.0.0.0",
        Port : 32217,
        YggdrasilServers : [
            {
                //! Mojang 官方验证服务器
                //? 一般来说官方服务器优先级最高 但是你可以不用官方验证服务器 直接注释掉即可
                Level : 0,
                Name: "Mojang",
                //! 服务器等级 越小优先级越高
                Url : "https://sessionserver.mojang.com"
            },
            {
                //! 第三方验证服务器案例 LittleSkin
                Level : 1,
                Name: "LittleSkin",
                //! 注意这个URL格式! 和大部分皮肤站提供的不太一样
                //? 多了    /sessionserver  一截
                Url : "https://littleskin.cn/api/yggdrasil/sessionserver"
            }
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


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
