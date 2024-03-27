# -*- coding: UTF-8 -*-
import discord
import psutil
from datetime import datetime
from discord.ext import commands

from classes import Slash_Cogs
from ui.view import *
from core.utils import colors,icon,utils,emojis

class slash_General(Slash_Cogs):
    @commands.command(name="help")
    async def help(self, ctx: commands.Context):
        view=HelpView()
        
        embed=discord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.set_author(name="Luminara使用指南",icon_url=icon.guide_icon_url,url="https://blog.earthlyeric6.ml/")
        embed.add_field(name="Hello，我是Luminara，很高興見到你!",value="你可以從下面選擇想看的指令使令用法類別。")
        embed.set_footer(text="Luminara")

        return await ctx.reply(embed=embed,view=view)