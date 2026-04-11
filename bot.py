import discord
from discord.ext import commands
import os
from model import get_class
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR,exist_ok=True)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def hehe(ctx, count_he = 5):
    await ctx.send("he" * count_he)
@bot.command()
async def analiz(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            file_path = os.path.join(IMAGE_DIR, file_name)
            await i.save(file_path)
            await ctx.send("Görseliniz save noktasına ulaştı. <3")
            class_name, score = get_class(img=file_path)
            await ctx.send(f"Görselinizin sınıfı: {class_name} Tahmini skor: %{score}")
            if class_name == 'dog':
                await ctx.send('''Kaliteli Köpek Maması: Köpeklerin sağlıklı kalması için protein, vitamin ve mineral içeren hazır mamalar en güvenli yoldur. Yavru köpekler için "junior", yetişkinler için "adult" mamalar tercih edilmelidir.

Öğün Düzeni: Yavru köpekler genellikle günde 3-4 öğün, yetişkin köpekler ise günde 2 öğün beslenir. Mamayı her gün aynı saatlerde vermek sindirim sistemleri için iyidir.

Taze Su: Köpeğinin önünde her zaman temiz ve taze su bulunmalıdır.

Yasaklı Gıdalar: Bazı yiyecekler köpekler için çok tehlikelidir. Bunlardan uzak tutmalısın:

Çikolata ve şekerli gıdalar

Soğan ve sarımsak

Üzüm ve kuru üzüm

Pişmiş tavuk kemikleri (boğazına kaçabilir veya batabilir)''')
            else:
                await ctx.send('''Etçil Beslenme: Kediler "zorunlu etçildir", yani vücutlarının ihtiyaç duyduğu temel maddeleri (özellikle taurin) sadece hayvansal proteinlerden alabilirler. Bu yüzden kaliteli kedi maması kullanmak çok önemlidir.

Öğün Sayısı: Kediler genellikle gün boyu küçük porsiyonlar halinde yemeyi severler. Kuru mamayı gün boyu ulaşabileceği bir yerde bırakabilir veya sabah-akşam olacak şekilde öğünlere bölebilirsin.

Yaş Mama Desteği: Kediler doğaları gereği çok az su içerler. Böbrek sağlığını korumak için haftada birkaç kez yaş mama vermek, su ihtiyaçlarını karşılamaya yardımcı olur.

Yasaklı Gıdalar: Kedine asla vermemen gereken bazı yiyecekler:

Süt: Çoğu kedi yetişkin olduğunda laktozu sindiremez ve karnı ağrıyabilir.

Çiğ Et/Balık: Parazit veya bakteri riski taşır.

Çikolata ve Kafein: Kediler için zehirli olabilir.

Soğan ve Sarımsak: Kan hücrelerine zarar verebilir.''')
    else:
        await ctx.send("Görselinizi save noktasına ulaşamadı.  ")
bot.run("TOKEN HERE") 