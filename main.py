import discord
from dotenv import dotenv_values

def main():
    class ArkClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

    try:
        env = dotenv_values('.env')
        print(env['API_TOKEN'])
    except KeyError:
        print("""
            Could not find 'API_TOKEN'.\n
            Make sure your .env is configured correctly.
            """)

    intents = discord.Intents.default()
    client = ArkClient(intents=intents)
    client.run(env['API_TOKEN'])


if __name__ == "__main__":
    main()
