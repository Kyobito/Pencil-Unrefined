import discord
from discord.ext import commands, tasks
import os
from ping import keep_alive
import time
import asyncio
import manual
import math
import requests
import calc
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import help_user
from replit import db
import sched

from random import choice

#---------------------------------------
# Intents
intents = discord.Intents.default()
intents.members = True
#---------------------------------------
client = commands.Bot(command_prefix='>', help_command=None, intents=intents)
#---------------------------------------
# Basic Commands

status = ['rhythm games', 'piano','music']

welcome = ['Howdy!','Hello!','Hi!','Aloha!']

embed_color = discord.Color.blue()

perm_warning = "You do not have proper permissions"

curse_list = ['fuck','shit','dumbass','@everyone','@here']

curse_replies = ["Watch your mouth you animal", "Don't say that!", "That's a no-no word"]

h_bool = False

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(">help"))
  print('{0.user} is ready'.format(client))

def ad(phrase):
  title = '**'
  for first in range(0,math.floor((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+=phrase
  for last in range(0,math.ceil((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+='**'
  return title

def cut(phrase):
  list_of_words = phrase.split()
  return list_of_words

def rank_convert(phrase):
  if '_PLUS' in phrase:
    phrase = phrase.replace('_PLUS','+')
  if 'SUPERSTAR' in phrase:
    phrase = 'MVP++'
  phrase = phrase.title()
  return phrase

def h_timer(num):
  global h_bool
  time.sleep(num)
  h_bool = False
  return h_bool

def shave(num):
  num = str(num)
  new_num = ''
  for i in range(0,10):
    new_num += num[i]
  return int(new_num)

hak = os.environ['HYPIXEL_API_KEY']

def cdtchange(date,time):
    apart = time.split(':')
    hours = int(apart[0])
    minutes = int(apart[1])
    seconds = int(apart[2])
    
    divided = date.split('-')
    years = int(divided[0])
    months = int(divided[1])
    days = int(divided[2])

    utc = pytz.utc
    loc_dt = utc.localize(datetime(years, months, days, hours, minutes, seconds))
    
    central = timezone('America/Chicago')
    cst_dt = loc_dt.astimezone(central)
    return cst_dt.strftime('%Y-%m-%d %H:%M:%S %Z')
#---------------------------------------
# Events
@client.event
async def on_member_join(member):
  join_channel = os.environ['JOIN_CHANNEL_ID']
  channel = client.get_channel(int(join_channel))
  await channel.send(f'{member.mention} has joined the server. Say hello!')

@client.event
async def on_member_remove(member):
  join_channel = os.environ['JOIN_CHANNEL_ID']
  channel = client.get_channel(int(join_channel))
  await channel.send(f'{member.mention} has left the server...')

@client.event
async def on_message_delete(message):
  db["last"] = message.content
  db["last_author"] = message.author.mention

#---------------------------------------
@client.command(name='help')
async def help2(ctx):
  global embed_color
  await ctx.send(embed=help_user.helper(embed_color))

@client.command(name='hypixel')
async def hypixel(ctx, specify, player_name=None):
  global h_bool
  if specify == 'links':
    if player_name is None:
      link_embed = discord.Embed(title='Links', description='Links to resources used.\n',color = discord.Color.default())
      link_embed.set_image(url='https://i.imgur.com/6Pa0jiS.png')
      await ctx.send(embed=link_embed)
  elif specify == 'stats':
    if h_bool == False:
      if player_name is None:
        await ctx.send('You did not specify a player!')
      else:
        url = f'https://api.mojang.com/users/profiles/minecraft/{player_name}?'
        response = requests.get(url)
        h_response = requests.get(
          url = "https://api.hypixel.net/key",
          params = {
            "key": hak
          }
        ).json()
        queries = h_response['record']['queriesInPastMin']
        if queries > 99:
          await ctx.send("**You have exceeded the 100 requests per minute allowed by the bot. Please wait until the next minute**")
          h_bool = True
          h_timer(60)
        else:
          try:
            player_uuid = response.json()['id']
            hypixel_data = requests.get(
            url = "https://api.hypixel.net/player",
            params = {
              "key": hak,
              "uuid": player_uuid
            }
            ).json()
            stats_embed = discord.Embed(title = player_name+"'s stats", description=' ', color = discord.Color.default())
            user = ctx.author
            stats_embed.set_footer(text='Requested by: ' + str(user))
            stats_embed.set_thumbnail(url='https://i.imgur.com/6Pa0jiS.png')

            # Basic Player information
            net_xp = hypixel_data['player']['networkExp'] if 'networkExp' in hypixel_data["player"] else 0
            net_level = str(calc.netexp_to_level(net_xp))
            ach_points = str(hypixel_data['player']['achievementPoints']) if 'achievementPoints' in hypixel_data["player"] else "0"
            karma = str(hypixel_data['player']['karma']) if 'karma' in hypixel_data["player"] else "0"
            stats_embed.add_field(name="**Basic Information**",value="**Name: **" + player_name + "\n**Network Level: **"+ net_level + "\n**Achievement Points: **"+ach_points+"\n**Karma: **"+ karma,inline = True)

            # Recent game
            recent = str(hypixel_data['player']['mostRecentGameType']).title() if 'mostRecentGameType' in hypixel_data["player"] else "Wow there's nothing"
            if recent == 'Walls3':
              recent = 'Mega Walls'
            stats_embed.add_field(name='Recent Game Type',value=recent, inline = True)

            # Rank
            if "rank" in hypixel_data["player"] and not hypixel_data["player"]["rank"] == "NORMAL":
              rank = hypixel_data["player"]["rank"]
            elif "monthlyPackageRank" in hypixel_data["player"] and not hypixel_data["player"]["monthlyPackageRank"] == "NONE":
              rank = hypixel_data["player"]["monthlyPackageRank"]
            elif "newPackageRank" in hypixel_data["player"]:
              rank = hypixel_data["player"]["newPackageRank"]
            elif "packageRank" in hypixel_data["player"]:
              rank = hypixel_data["player"]["packageRank"]
            else:
              rank = None
            if rank is None:
              rank = 'Default'
            else:
              rank = rank_convert(rank)
            stats_embed.add_field(name='Rank',value=rank, inline=True)

            # Status
            last_out = hypixel_data['player']['lastLogout'] if 'lastLogout' in hypixel_data["player"] else 0
            if last_out != 0:
              last_out = shave(last_out)
            last_in = hypixel_data['player']['lastLogin'] if 'lastLogin' in hypixel_data["player"] else 0
            if last_in != 0:
              last_in = shave(last_in)

            con_out_date = time.strftime('%Y-%m-%d', time.gmtime(last_out))
            con_out_time = time.strftime('%H:%M:%S', time.gmtime(last_out))
            con_in_date = time.strftime('%Y-%m-%d', time.gmtime(last_in))
            con_in_time = time.strftime('%H:%M:%S', time.gmtime(last_in))

            con_out = cdtchange(con_out_date,con_out_time)
            con_in = cdtchange(con_in_date,con_in_time)
            if last_in == 0:
              con_in = 'Unknown'
            if last_out == 0:
              con_out = 'Unknown'
            status_val = 'Online' if last_in > last_out else 'Offline'
            stats_embed.add_field(name='**Status**', value = '**Current Status: **' + status_val + '\n**Last Login: **' + con_in + '\n**Last Logout: **'+con_out, inline=True)

            # BedWars
            if 'Bedwars' in hypixel_data['player']['stats']:
              bed_xp = hypixel_data['player']['stats']['Bedwars']['Experience'] if 'Experience' in  hypixel_data['player']['stats']['Bedwars'] else 0
              bed_lvl = str(calc.bedexp_to_level(bed_xp))
              bed_coins = str(hypixel_data['player']['stats']['Bedwars']['coins']) if 'coins' in hypixel_data['player']['stats']['Bedwars'] else "0"
              bed_kills = str(hypixel_data['player']['stats']['Bedwars']['kills_bedwars']) if 'kills_bedwars' in hypixel_data['player']['stats']['Bedwars'] else "0"
              bed_wins = str(hypixel_data['player']['stats']['Bedwars']['wins_bedwars']) if 'wins_bedwars' in hypixel_data['player']['stats']['Bedwars'] else "0"
              stats_embed.add_field(name='**Bedwars**',value='**Level: **'+bed_lvl+'\n**Coins: **' + bed_coins+'\n**Lifetime Kills: **' + bed_kills+'\n**Lifetime Wins: **'+bed_wins,inline=True)
            else:
              stats_embed.add_field(name='**Bedwars**',value='No Bedwars data!',inline=True)
              
            # SkyWars
            if "SkyWars" in hypixel_data["player"]['stats']:
              sky_exp = hypixel_data["player"]["stats"]["SkyWars"]["skywars_experience"] if "skywars_experience" in hypixel_data["player"]["stats"]["SkyWars"] else 0
              sky_level = str(calc.sw_xp_to_lvl(sky_exp))
              sky_kills = str(hypixel_data["player"]["stats"]["SkyWars"]["kills"]) if 'kill' in hypixel_data["player"]["stats"]["SkyWars"] else '0'
              sky_wins = str(hypixel_data["player"]["stats"]["SkyWars"]["wins"]) if 'wins' in hypixel_data["player"]["stats"]["SkyWars"] else '0'
              sky_sg = str(hypixel_data["player"]["stats"]["SkyWars"]["souls_gathered"]) if "souls_gathered" in hypixel_data["player"]["stats"]["SkyWars"] else '0'
              sky_ct = str(hypixel_data["player"]["stats"]["SkyWars"]["cosmetic_tokens"]) if "cosmetic_tokens" in hypixel_data["player"]["stats"]["SkyWars"] else '0'
              sky_coins = str(hypixel_data["player"]["stats"]["SkyWars"]["coins"]) if "coins" in hypixel_data["player"]["stats"]["SkyWars"] else '0'
              stats_embed.add_field(name='**SkyWars**',value='**Level: **' + sky_level + '\n**Coins: **'+sky_coins+'\n**Lifetime Wins: **'+sky_wins+'\n**Lifetime Kills: **'+sky_kills+'\n**Lifetime Souls: **'+sky_sg+'\n**Current Tokens: **'+sky_ct, inline = True)
            else:
              stats_embed.add_field(name='**SkyWars**',value='No SkyWars data!',inline=True)
            
            # Mega Walls
            if 'Walls3' in hypixel_data['player']['stats']:
              mw_coin = str(hypixel_data['player']['stats']['Walls3']['coins']) if 'coins' in hypixel_data['player']['stats']['Walls3'] else '0'
              tot_kills = str(hypixel_data['player']['stats']['Walls3']['kills']) if 'kills' in hypixel_data['player']['stats']['Walls3'] else '0'
              tot_fn = str(hypixel_data['player']['stats']['Walls3']['final_kills']) if 'final_kills' in hypixel_data['player']['stats']['Walls3'] else '0'
              mw_wins = str(hypixel_data['player']['stats']['Walls3']['wins']) if 'wins' in hypixel_data['player']['stats']['Walls3'] else '0'
              stats_embed.add_field(name='**Mega Walls**',value='Coins: ' + mw_coin + '\nLifetime Kills: ' + tot_kills + '\nLifetime Final Kills: ' + tot_fn + '\nLifetime Wins: '+ mw_wins,inline=True)
            else:
              stats_embed.add_field(name='**Mega Walls**',value='No Mega Walls data!',inline=True)

            # Build Battle
            if 'BuildBattle' in hypixel_data['player']['stats']:
              bb_score = str(hypixel_data['player']['stats']['BuildBattle']['score']) if 'score' in hypixel_data['player']['stats']['BuildBattle'] else '0'
              bb_coins = str(hypixel_data['player']['stats']['BuildBattle']['coins']) if 'coins' in hypixel_data['player']['stats']['BuildBattle'] else '0'
              bb_wins = str(hypixel_data['player']['stats']['BuildBattle']['wins']) if 'wins' in hypixel_data['player']['stats']['BuildBattle'] else '0'
              stats_embed.add_field(name='**Build Battle**', value = 'Score: '+bb_score+'\nCoins: '+bb_coins+'\nLifetime Wins: ' + bb_wins, inline = True)
            else:
              stats_embed.add_field(name='**Build Battle**', value = 'No Build Battle data!', inline = True)
            # Send Stats
            await ctx.send(embed=stats_embed)
          except KeyError:
            await ctx.send("This player does not exist or there is a missing value")
    else:
      await ctx.send('Please wait until the query data is reset')
      
@client.command(name='suggest')
async def suggest(ctx, words):
  # Assuming that there is a 'Requests' channel
  secret = os.environ['REQUEST_ID']
  channel = client.get_channel(int(secret))
  await channel.send(words)

@client.command(name='closure')
async def closure(ctx):
  await ctx.send('This channel is marked for closure. Channel will be put in archived if no messages are sent in the next 2 weeks')
  time.sleep(5)
  await ctx.message.delete()

@client.command(name='purge')
async def purge(ctx, amount):
  if ctx.author.guild_permissions.administrator:
    await ctx.channel.purge(limit=int(amount))
    await ctx.send(amount + " messages were purged by " + f'{ctx.author.mention}')
  else:
    await ctx.send("You do not have proper permissions!")

@purge.error
async def error_purge(ctx, error):
  if isinstance(error, commands.DisabledCommand):
    await ctx.send("This command is disabled")

@client.command(name='ping')
async def ping(ctx):
  print("'Ping' command initiated")
  ping_page = discord.Embed(title='', description=f' **Latency: {round(client.latency * 1000)}ms**', color=embed_color)
  await ctx.send(embed=ping_page)

  
@client.command(name='custom')
async def custom(ctx, *, printer=None):
  print("'Custom' command initiated")
  if printer is None:
    await ctx.send("You did not enter anything!")
    raise Exception("Conditions were not met")
  else: 
    print("'Custom' command initiated")
    await ctx.send(printer)
    
@client.command(name='about')
async def about(ctx):
  print("'About' command initiated")
  about_page = discord.Embed(title='About', description="Pencils is a bot made specifically for the IEatPencils server. However, the bot is still accessible and is open source through the Repl.it website. The URL won't be here though so that's for you to find! :smile: ", color=embed_color)
  about_page.add_field(name='Language', value='This bot was created using python and the discord.py API!',inline=False)
  about_page.add_field(name='Documentation', value='Pencils is documented using Git on the GitHub host.', inline = True)
  about_page.add_field(name='Connection', value='Pencils is online 24/7 (except during development) using the monitoring service UpTimeRobot',inline=True)
  about_page.add_field(name='Note', value='All resources used in the development of this bot are free.',inline=False)
  await ctx.send(embed=about_page)

@client.command(name='announce')
async def announce(ctx, announce_title, announce_description, url_input=None):
  print("'Announce' command initiated")
  announce_embed=discord.Embed(title=announce_title, description=announce_description, color=embed_color)
  announce_embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
  await ctx.send(embed=announce_embed)
  if url_input != None:
    for i in cut(url_input):
      print('Image sent')
      announce_embed=discord.Embed(title='', description='', color=discord.Color.default())
      announce_embed.set_image(url=i)
      await ctx.send(embed=announce_embed)
  time.sleep(5)
  await ctx.message.delete()
  
@client.command(name='man')
async def man(ctx, specify):
  print("'Man' command initiated")
  await ctx.send(manual.syntax(specify))

@client.command(name='disable')
async def disable(ctx, specify):
  if ctx.author.guild_permissions.administrator:
    '''if specify == 'spam':
      cmd = client.get_command('spam')
      cmd.update(enabled=False)
      await ctx.send("Command has been disabled")'''
    if specify == 'purge':
      cmd = client.get_command('purge')
      cmd.update(enabled=False)
      await ctx.send("Command has been disabled")
  else:
    await ctx.send(perm_warning)

@client.command(name='enable')
async def enable(ctx, specify):
  if ctx.author.guild_permissions.administrator:
    '''if specify == 'spam':
      cmd = client.get_command('spam')
      cmd.update(enabled=True)
      await ctx.send("Command has been enabled")'''
    if specify == 'purge':
      cmd = client.get_command('purge')
      cmd.update(enabled=True)
      await ctx.send("Command has been enabled")
  else:
    await ctx.send(perm_warning)

@client.command(name='snipe')
async def snipe(ctx):
  last_deleted = db["last"]
  last_deleted_author = db["last_author"]
  if not any(i in last_deleted for i in curse_list):
    await ctx.send(last_deleted_author+ ": "+last_deleted)
  else:
    await ctx.send('The message had a blacklisted word!')

#Go to calendar.py and copy and paste code back here if you wish

@client.command(name='pfp')
async def pfp(ctx, persona:discord.User = None):
  iep = client.get_guild(int(os.getenv('IEP_SERVER_ID'))) #IEP exclusive command
  if iep.get_member(persona.id if persona is not None else None) is not None:
    await ctx.send(persona.avatar_url)
  elif persona is None:
    await ctx.send(ctx.author.avatar_url)
  
@pfp.error
async def pfp_error(ctx, error):
  if isinstance(error, discord.ext.commands.errors.UserNotFound):
    await ctx.send('This user does not exist!')

@client.command(name='flip')
async def flip(ctx):
  num_list = [1,2]
  chosen = choice(num_list)
  if chosen == 1:
    await ctx.send("You got **Heads!**")
  elif chosen == 2:
    await ctx.send("You got **Tails!**")
  else:
    await ctx.send("Something went wrong...")

@client.command(name='roll')
async def roll(ctx):
  num_list = [1,2,3,4,5,6]
  chosen = choice(num_list)
  await ctx.send("You rolled **" + str(chosen) + '**')

@client.command(name='valorant')
async def valorant(ctx, specify):
  if specify == 'map':
    map_list = ['Fracture','Bind','Breeze','Split','Icebox','Haven','Ascent']
    chosen = choice(map_list)
    await ctx.send("Your map is **" + chosen + '**')
  elif specify == 'agent':
    agent_list = ['Sage','Jett','Brimstone','Astra','Phoenix','Omen','KAY/O','Viper','Yoru','Skye','Killjoy','Reyna','Sova','Cypher','Breach','Raze', 'Neon', 'Chamber']
    chosen = choice(agent_list)
    await ctx.send("Your agent is **" + chosen + '**')
  else:
    await ctx.send("That command doesn't exist!")

@client.command(name='ding')
async def ding(ctx, specify):
  iep = client.get_guild(int(os.getenv('IEP_SERVER_ID')))
  if specify == "valorant":
    valorant = iep.get_role(int(os.getenv('VALORANT_ROLE_ID')))
    if iep.get_role(valorant.id if valorant.id is not None else None) is not None:
      await ctx.send(valorant.mention)
  elif specify == "testing":
    testing = iep.get_role(int(os.getenv('TESTING_ROLE_ID')))
    if iep.get_role(testing.id if testing.id is not None else None) is not None:
      await ctx.send(testing.mention)
#--------------------------------------
keep_alive()
client.run(os.getenv('TOKEN'))