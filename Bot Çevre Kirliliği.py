import discord
from discord.ext import commands
from tokenignore import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def yardım(ctx):
    await ctx.send("Çevre kirliliği tanımı için !ÇevreKirliliğiTanım, çevre kirliliğini önlemek için yapılabilecek uygulamaları öğrenmek için !KirlilikNasılÖnlenir, atıkların geri dönüşüm ayrışması hakkında bilgi almak için !GeriDönüşüm yazınız.")
@bot.comand()
async def ÇevreKirliliğiTanım(ctx):
    await ctx.send('Çevre kirliliği, çevrenin doğal olmayan bir şekilde insan eliyle doğallığının bozulmasıdır. Bu ekosistemi bozma eylemleri; kirlenme şeklinde tabir edilmektedir.')
@bot.command()
async def KirlilikNasılÖnlenir(ctx):
    await ctx.send('```Çevre kirliliğini önlemek için bazı örnekler:```')
    await ctx.send('1. Çevre konusunda bilgi edinin.')
    await ctx.send('2. Kirliliğe engel olun. ')
    await ctx.send('3. Atıklarınızı ayrıştırın, geri dönüşüme katkı sağlayın.')
    await ctx.send('4. Naylon poşet kullanımını azaltın.')
    await ctx.send('5. Kâğıt havlu kullanımını azaltın.')
    await ctx.send('6. Dişinizi fırçalarken, banyo yaparken ve mutfakta çeşmeyi açık bırakmayın.')
    await ctx.send('7. Enerji tasarruflu ampuller kullanın.')
    await ctx.send('8. Atık pilleri çöpe değil, atık pil kutusuna atın.')
    await ctx.send('9. Bitkisel atık yağları, çöpe ya da lavaboya dökmeyin. En yakın atık yağ toplama bidonuna atın.')
    await ctx.send('10. Yazışmalarınızda çıktı almamaya dikkat edin, e-posta kullanın.')
@bot.command()
async def GeriDönşümBilgi(ctx):
    await ctx.send("Geri dönüşüm, atıkların doğaya zarar vermeden yeniden kullanılabilir hale getirilmesi sürecidir. Bu süreç, çevre kirliliğini azaltır, doğal kaynakları korur ve enerji tasarrufu sağlar. Geri dönüşüm, plastik, kağıt, cam ve metal gibi malzemelerin yeniden işlenmesini kapsar.")
bot.run(token)