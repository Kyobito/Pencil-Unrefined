'''@client.command(name='caesar')
async def caesar(ctx, word, base):
  await ctx.send("The word '" + word + "' with a shift of '" + base + "' is **" + encode.caesar_cipher(word, int(base))+"**")

@client.command(name='sub')
async def sub(ctx, word, substitute, specify):
  await ctx.send("New word: **"+ encode.substitution(word,substitute,specify)+"**")


Warning: might cause rate limit exception
@client.command(name='spam')
async def spam(ctx, phrase, amount, speed):
  if ctx.author.guild_permissions.administrator:
    await ctx.send("Are you sure you want to do this? [y/n]")
    def check(prompt):
      return (prompt.content.lower() in ['y','n']) and (prompt.author == ctx.author)
    try:
      msg= await client.wait_for('message',check=check,timeout=10.0)
      if msg.content.lower() == "y":
        for i in range(int(amount)):
          time.sleep(float(speed))
          await ctx.send(phrase)
      elif msg.content.lower() == "n":
        await ctx.send("Shutting down...")
    except asyncio.TimeoutError:
      await ctx.send("You did not enter anything!")
  else:
    await ctx.send("You do not have proper permissions!")

@spam.error
async def error_spam(ctx, error):
  if isinstance(error, commands.DisabledCommand):
    await ctx.send("This command is disabled")

@client.command(name='binary')
async def binary(ctx, number):
  await ctx.send("Binary number: **" + encode.binary(int(number))+"**")

@client.command(name='hexa')
async def hexa(ctx, number):
  await ctx.send("Hexadecimal number: **" +encode.hexadecimal(number)+"**")

@client.command(name='hello')
async def hello(ctx):
  print("'Hello' command initiated")
  await ctx.send(choice(welcome))

@client.command(name='reverse')
async def reverse(ctx, line):
  print("'Reverse' command initiated")
  await ctx.send(line[::-1])

Broken
@client.command(name='upcoming')
async def upcoming(ctx, specify, day=None, insert=None):
  if specify == 'view':
    current_week = datetime.date.today()
    year, week, day = current_week.isocalendar()
    up_embed = discord.Embed(title='Upcoming',description='Week '+ str(week) +' of the year', color = discord.Color.blue())

    ultimate_sunday = ''
    for i, x in db["up_sunday"], len(db["up_sunday"]):
      ultimate_sunday += db["up_sunday"][i] + ' \n'
    # Enter retrieval of days of the week

    up_embed.add_field(name='Sunday', value=ultimate_sunday,inline=False)

    await ctx.send(embed=up_embed)
  if specify == 'add':
    if day == 'Sunday':
      if db["sunday_count"] is None:
        sunday_values = 0
      else:
        sunday_values = int(db["sunday_count"])
      db["up_sunday"][sunday_values] = insert
      sunday_values = int(db["sunday_count"])+1
      db["sunday_count"] = sunday_values

Troll Command:
@client.command(name='report')
async def report(ctx, persona:discord.User = None):
  iep = client.get_guild(int(os.getenv('IEP_SERVER_ID'))) #IEP exclusive command
  if iep.get_member(persona.id if persona is not None else None) is not None:
    await ctx.send(str(persona) + " has been reported. Your messages over the past hour have been recorded and has been given to the FBI.");
  else:
    await ctx.send("Player does not exist or error");

@client.command(name='credits')
async def credits(ctx, specify, persona:discord.User = None, amount = None):
  iep = client.get_guild(int(os.getenv('IEP_SERVER_ID')))
  if specify == 'leaderboard' or specify == 'lb':
    #ffff 
    #for i in db["credit_players"][str(persona)]:
      
    await ctx.send("China")
  elif specify == 'award':
    if ctx.author.guild_permissions.administrator:
      if iep.get_member(persona.id if persona is not None else None) is not None:
        try:
          if amount == None:
            await ctx.send("You didn't specify an amount or number not sent")
          elif isinstance(int(amount), int):
            #db["greeting"] = {}
            #temp = db["greeting"]
            #temp["nested"] = "hi"
            #db["greeting"] = temp
            #print(db["greeting"]["nested"])
            '''db["credit_players"] = {}
            temp = db["credit_players"]
            temp[str(persona)]+= amount
            db["credit_players"] = temp'''

            #db["credit_players"][str(persona)]["money"]+=int(amount)
            #db["credit_players"][str(persona)]["user"] = str(persona)
            await ctx.send("You have awarded credits " + amount + " to " + str(persona) + '!')
        except ValueError:
          await ctx.send("Number was not sent?")
      else:
        await ctx.send("You didn't specify anybody or error")
    else:
      await ctx.send("You can't do that!")

Listener: DO NOT USE | RATE LIMIT EXCEPTION
@client.listen('on_message')
async def curse(ctx):
  current_channel = ctx.channel
  for i in curse_list:
    if i in ctx.content.lower():
      await current_channel.send(f'{ctx.author.mention} ' +choice(curse_replies))
'''