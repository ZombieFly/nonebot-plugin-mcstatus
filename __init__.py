from nonebot.plugin import on_shell_command
from nonebot.params import ShellCommandArgs
from nonebot.adapters.onebot.v11 import (
    MessageEvent,
    PrivateMessageEvent,
    GroupMessageEvent,
)

from .parser import mc_parser, ArgNamespace
from .handle import Admin_Handle, Anyone_Handle

# 注册 shell_like 事件响应器
mcs = on_shell_command("mcs", parser=mc_parser, priority=5)


@mcs.handle()
async def _(event: MessageEvent,  args: ArgNamespace = ShellCommandArgs()):
    args.user_id = event.user_id if isinstance(event, PrivateMessageEvent) else None
    args.group_id = event.group_id if isinstance(event, GroupMessageEvent) else None
    args.is_admin = (
        event.sender.role in ["admin", "owner"]
        if isinstance(event, GroupMessageEvent)
        else False
    )
    if hasattr(args, "handle"):
        try:
            #优先尝试执行Anyone权限命令
            result = await getattr(Anyone_Handle, args.handle)(args)
            if result:
                await mcs.finish(result)
        except AttributeError:
            if args.is_admin:
                #尝试执行Admin权限命令
                result = await getattr(Admin_Handle, args.handle)(args)
                if result:
                    await mcs.finish(result)
            await mcs.finish('不存在对应命令，请检查命令是否存在，或者是否具有相应执行权限')
                
# nonebot_help

__usage__ = '''Minecraft Server Checker
/mcs add <name> <address>  #为本群记录一个服务器，将自动判断服务器类型（形如/mcs add demo example.org）
/mcs list  # 展示本群已记录服务器列表
/mcs remove <name>  # 删除对应服务器
/mcs ping <name>  # 检查对应服务器的状态
/mcs p  # 检查列表第一个服务器的状态
'''

__version__ = '0.1.0'

__plugin_name__ = "Minecraft Server Checker"
