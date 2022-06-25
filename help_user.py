import discord
import math

def ad(phrase):
  title = '**'
  for first in range(0,math.floor((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+=phrase
  for last in range(0,math.ceil((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+='**'
  return title

def helper(color):
  print("'Help' command initiated")
  help_page = discord.Embed(title='Help Page', description ='\n',color = discord.Color.blue())
  help_page.add_field(name=ad("Basic Commands"),value='Every day commands',inline=True)
  help_page.add_field(name='ping', value = 'Returns bot-command latency', inline=False)
  help_page.add_field(name='hello', value = 'Sends a greeting', inline=False)
  help_page.add_field(name='about', value = 'Sends information regarding the bot', inline=False)
  help_page.add_field(name='man', value = 'Sends syntax of a specified command', inline=False)
  help_page.add_field(name='custom', value = 'Sends user-inputted text back', inline=False)
  help_page.add_field(name='announce', value = 'Sends user-inputted data in embedded form', inline=False)
  help_page.add_field(name='suggest', value = 'Sends a request to the moderators', inline = False)  
  help_page.add_field(name='snipe', value = "Sends the last deleted message", inline = False)
  help_page.add_field(name="pfp", value="Sends a specified user's profile picture", inline = False)
  help_page.add_field(name="flip", value="Flips a coin and sends output", inline = False)
  help_page.add_field(name="roll", value="Rolls a dice and sends output", inline = False)
  help_page.add_field(name="valorant", value = "Parameters: agent (Chooses an agent and sends output) | map (Chooses a map and sends output)", inline = False)
  help_page.add_field(name="ding", value = "Pings a certain server role | Options: valorant, testing", inline = False)
  help_page.add_field(name=ad("Administrator commands"), value='Commands that required administrator permissions', inline=True)
  help_page.add_field(name="disable", value="Will disable other administrator commands", inline  = False)
  help_page.add_field(name="enable",value="Will enable any disabled administrator command", inline = False)
  help_page.add_field(name="closure", value="Sends a message stating a channel's closure", inline = False)  
  help_page.add_field(name="purge", value="Purges a bunch of messages", inline = False) 
  help_page.add_field(name=ad("Hypixel Commands"), value = 'Commands used with Hypixel API', inline = True)
  help_page.add_field(name="Note", value = "You must use the command '>hypixel' and specify the second parameter using these 'sub' commands", inline = False)
  help_page.add_field(name="stats", value = "Sends the stats of the specified player. The name of the player must be officially registered on the Minecraft System", inline = False)
  help_page.add_field(name="links", value = "Sends the links used in the development of this command | Currently not present", inline = False)
  
  return help_page