import wavelink
import nextcord
import bot
from nextcord.ext import commands
from core.classes import CogTop
from core.config import *
from core.lib  import *

class Music(CogTop):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot:commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """連線到Lavalink節點"""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
            host='us01.lavalink.reload-dev.ml',
            port=443,
            password='1A6DCEE7A27DA826B313FBC562CD2',
            identifier='Public US Main VPS 01',
            https=True,
            )

        await wavelink.NodePool.create_node(bot=self.bot,
            host='51.161.130.134',
            port=10414,
            password='1A6DCEE7A27DA826B313FBC562CD2',
            identifier='Public Asia Main VPS 01',
            )
        
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lava.link',
            port= 80,
            password='anything as a password',
            identifier='Public EU Main 01',
            )
        await wavelink.NodePool.create_node(bot=self.bot,
            host='lavalink.oops.wtf',
            port= 2000,
            password='www.freelavalink.ga',
            identifier='Public Asia Main 01',
            )
    @commands.Cog.listener()
    async def on_wavelink_track_end(self,player:wavelink.Player,track: wavelink.Track):
        ctx = player.ctx
        vc: player = ctx.voice_client

        next_song = vc.queue.get()

        await vc.play(next_song)
        await ctx.send(f"即將播放下一首 {next_song.title}")

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, track:wavelink.YouTubeTrack):
        await ctx.send('<:loading:1001057291036020776> 搜尋歌曲中...',delete_after=3)

        if not ctx.voice_client:
            vc: wavelink.Player=await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player=ctx.voice_client


        embed=nextcord.Embed(title=':white_check_mark: 已新增至播放清單 !')
        embed.add_field(name='%s'% (track.title),value='From Youtube',inline=False)
        embed.set_footer(text=f'Lost', icon_url=bot.icon_url)
        await ctx.reply(embed=embed)

        if vc.queue.is_empty and  vc.is_playing:
            await vc.play(track)
        else:
            await vc.queue.put_wait(track)


    @commands.command()
    async def leave(self,ctx:commands.Context):
        vc: wavelink.Player=await ctx.voice_client.disconnect()
        embed=nextcord.Embed(title=f':no_entry: 已被{ctx.author.name}要求中斷連線')
        await ctx.reply(embed=embed)
    

def setup(bot):
    bot.add_cog(Music(bot))