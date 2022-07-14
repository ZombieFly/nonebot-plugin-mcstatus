### 本项目已独立于原仓库，移动至[nb-mcsc](https://github.com/ZombieFly/nb-mcsc)
### 本仓库Fork自[Nonebot Plugin MCStatus](https://github.com/nonepkg/nonebot-plugin-mcstatus)

基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 Minecraft 服务器状态查询插件

### 安装

#### 克隆此仓库至Nonebot生成的`plugins`文件夹中

`git clone https://github.com/ZombieFly/nonebot_plugin_mcstatus.git`

### 命令格式

`/mcs add <name> <address>`为所在群添加一个服务器记录，在不指定端口时，将依次检查基岩版服务器与Java版服务器默认端口上是否有开放服务器，如果存在，将连同服务器类型一同记录

`/mcs list`  展示所在群服务器记录

`/mcs remove <name>`  删除对应服务器

`/mcs ping <name>` 检查对应服务器的状态（仅依照添加时记录的服务器类型检查）

`/mcs p` 检查列表第一个服务器的状态

注：`/`为命令头，请依照具体设定替换

### 服务器状态返回样式

#### 基岩版

```
Title: {status.motd}-{status.map}
Version: {status.version.brand}{status.version.version}
Players: {status.players_online}/{status.players_max}
Gamemode: {status.gamemode}
```

#### Java版

```
Title: {cut_title}
Description: {cut_dc}	#当 status.description 中含有\n时，将以此切分为 Title 与 Description ，并自动去除首尾空格；反之仅有Title
Version: {status.version.name}
Players: {status.players.online}/{status.players.max}
```

### 帮助接入

已接入[nonebot-plugin-help](https://github.com/XZhouQD/nonebot-plugin-help)

### TODO

- [ ] 异步调用检查
- [ ] 设置置顶服务器
- [ ] 服务器开放探索（公开）
