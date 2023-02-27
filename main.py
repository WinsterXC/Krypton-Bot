import discord 
from discord import app_commands 
from discord.ext import commands 
import os 




bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

bot.remove_command('help')

@bot.event
async def on_ready():
  print("Bot is up and running!")
  try: 
    synced =await bot.tree.sync()
    print(f"Synced {len(synced)} commands(s)")
  except Exception as e: 
    print(e)

  await bot.change_presence(status=discord.Status.online, activity=discord.Game("/download"))


  
 


  

#Ping 
@bot.tree.command(name="ping", description="See the bot's latency")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message(f"Pong! `{round(bot.latency * 1000)}ms`")
  
   


@bot.tree.command(name="download", description="Download Project Krypton")
async def test(interaction: discord.Interaction):
  
   
  embed = discord.Embed(title="Project Krypton",description=f"""***Please download the required files below:***

**Microsoft Dotnet 3.1**
[Download Here](https://cdn.discordapp.com/attachments/679772336177545300/729408321769046026/dotnet-runtime-3.1.5-win-x64.exe).

**Node.js**
[Download Here](https://nodejs.org/dist/v19.7.0/node-v19.7.0-x64.msi).

**Fortnite Build Version**
This is the current Fortnite Version being hosted.
[Download Here](https://drive.google.com/file/d/1fNRu-NOAXBAI49NbxUAeaCNPznyW5JjX/view).
You can use EasyInstaller if prefered.

**Krypton Launcher**
Coming soon.

If there are any problems or issues please contact a helper in <#1077210540595761202>.""", colour=discord.Colour.purple())
  embed.set_footer(text = "Created By Winster. Version 1.1")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1079565548481953802/1079577772374110208/1.png")

  

  await interaction.response.send_message(f" {interaction.user.mention} Check your DM'S")
  user = bot.get_user(interaction.user.id)
  await user.send(embed=embed)
  

  
@bot.tree.command(name="help", description="Krypton Bot Help")
async def test(interaction: discord.Interaction):
  
   
  embed = discord.Embed(title="Project Krypton",description=f"""***Discord Bot Commands:***

**/ping**
Sends the bot's latency.

**/download**
Download Project Krypton!

""", colour=discord.Colour.purple())
  embed.set_footer(text = "Created By Winster. Version 1.1")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1079565548481953802/1079577772374110208/1.png")
  
  await interaction.response.send_message(embed=embed)

bot.run(os.environ["DISCORD_TOKEN"])


