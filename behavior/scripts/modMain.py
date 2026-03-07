# -*- coding: utf-8 -*-
from config import *
from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="MoreUI", version="0.0.1")
class MoreUI(object):
    @Mod.InitServer()
    def MoreUIServerInit(self):
        serverApi.RegisterSystem(NamespaceServer, SystemNameServer, SystemPathServer)

    @Mod.InitClient()
    def MoreUIClientInit(self):
        clientApi.RegisterSystem(NamespaceClient, SystemNameClient, SystemPathClient)
