# coding=utf-8
import mod.client.extraClientApi as clientApi

class A:
    pass

path = A.__module__
"""scripts.MoreUI.core.init_system"""
client_system_path = path.split("register")[0] + "core.client.MoreUIC.MoreUIClient"

clientApi.RegisterSystem("MoreUI", "MoreUIC", client_system_path)