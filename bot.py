import discord
import asyncio
import threading


INTENTS = discord.Intents.all()
# INTENTS = discord.Intents(messages=True, members=True, guilds=True)

class DiscordClient(discord.Client):
    def __init__(self):
        super(DiscordClient, self).__init__(intents=INTENTS)

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def get_connected_voice(self, channel_id):
        chnl = await self.fetch_channel(channel_id)
        ids = chnl.voice_states.keys() 

        members = []
        for id in ids:
            usr = await self.fetch_user(id)
            members.append(usr.display_name)
        return members

    
    async def on_message(self, ctx):
        if ctx.author == self.user:
            return
        if not ctx.content == '!whoson':
            return

        chnl = await self.fetch_channel(740393371021082793)
        ids = chnl.voice_states.keys() 
        print(ids)
        members = []
        for id in ids:
            usr = await self.fetch_user(id)
            members.append(usr.display_name)
        await ctx.channel.send(f'```{members}```')


async def test_loop(client:DiscordClient):
    while True:
        input('Press enter to run get_connected_voice')

        print(await client.get_connected_voice(740393371021082793))

if __name__ == '__main__':
    from prod import conf

    DISCORD_TOKEN = conf['discord']['bot_token'].get()


    client = DiscordClient()
    loop = asyncio.get_event_loop()
    loop.create_task(client.start(DISCORD_TOKEN))
    threading.Thread(target=loop.run_forever, daemon=True).start()
    # loop.run_forever()

    asyncio.run(test_loop(client))