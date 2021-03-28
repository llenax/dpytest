import os
from dotenv import load_dotenv
from app.main import client

load_dotenv()


if __name__ == "__main__":
  client.run(os.getenv("DISCORD_TOKEN"))