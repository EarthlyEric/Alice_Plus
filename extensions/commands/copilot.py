from discord.ext import commands
from sydney import SydneyClient
from discord.ext import commands

from core.libs.bot import Cogs

class Copilot(Cogs):
    @commands.hybrid_command(name="ask-ai", description="向AI詢問一個問題", with_app_command=True)
    async def ask_ai(self, ctx: commands.Context, question:str):
        async with ctx.typing():
            async with SydneyClient(use_proxy=True) as client:
                response = await client.ask(question)
                return await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Copilot(bot))