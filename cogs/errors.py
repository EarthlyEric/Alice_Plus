# -*- coding: UTF-8 -*-
import discord,asyncio
from discord.ext import commands
from discord.ext import *
from core.config import *
from core.classes import CogTop
from core.dbwork import *


class errors(CogTop):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f":question:  {ctx.author.name} 遺失必要參數 ",color=0xed0202)#Red
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"ALICE", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f":question:  {ctx.author.name} 未知錯誤 ",color=0xed0202)#Red
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"ALICE", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(errors(bot))
