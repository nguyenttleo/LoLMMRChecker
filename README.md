# LoLMMRChecker

LoLMMRChecker is a Discord bot that allows users to retrieve the MMR (Matchmaking Rating) of any League of Legends player within a Discord server. With this bot, you can easily check the skill level of players and get insights into their ranked performance.

## Project Overview

The LoLMMRChecker project includes the following file:

- `main.py`: This file contains the main logic and functionality of the LoLMMRChecker Discord bot. It handles interactions with the Discord API, retrieves player data from the League of Legends API, and provides MMR information in response to user commands.

## League of Legends (LoL)

League of Legends is a popular online multiplayer game developed and published by Riot Games. It falls under the category of MOBA (Multiplayer Online Battle Arena) games. In the game, players control a champion with unique abilities and work together in teams to defeat the opposing team's base.

MMR (Matchmaking Rating) is a hidden numerical value that represents a player's skill level in ranked matches. It determines the players they are matched with and the LP (League Points) gained or lost after each game. MMR serves as a measure of a player's relative skill in comparison to other players.

## How to Use LoLMMRChecker

To use the LoLMMRChecker Discord bot and retrieve MMR information, follow these steps:

1. Install the required dependencies:

   - Python: Make sure you have Python installed on your computer. You can download it from the official Python website (https://www.python.org).

2. Obtain a Discord API token:

   - Create a new Discord application and bot on the Discord Developer Portal (https://discord.com/developers/applications).

   - Copy the generated API token for later use.

3. Customize the bot settings:

   - Open the `main.py` file in a text editor.

   - Replace the placeholder values in the `TOKEN` and `GUILD` variables with your Discord API token and your Discord server's name, respectively.

4. Install the necessary Python dependencies:

   - Open a terminal or command prompt and navigate to the project directory.

   - Install the required dependencies by running the following command:

     ```bash
     pip install -r requirements.txt
     ```

5. Run the bot:

   - In the terminal or command prompt, navigate to the project directory.

   - Run the following command to start the LoLMMRChecker bot:

     ```bash
     python main.py
     ```

6. Add the bot to your Discord server:

   - Visit the Discord Developer Portal and go to your application's settings.

   - Generate an OAuth2 URL with the necessary permissions to invite the bot to your server.

   - Copy the generated URL and open it in a web browser.

   - Follow the on-screen instructions to add the bot to your server.

7. Use the bot:

   - In your Discord server, use the bot's command prefix (usually "!") followed by the command and the League of Legends summoner name you want to check. For example:

     ```plaintext
     !mmr Faker
     ```

   - The bot will retrieve and display the MMR information for the specified player in the server.

   - You can customize and extend the bot's functionality by modifying the `main.py` file according to your needs.

Now you can easily check the MMR of League of Legends players within your Discord server using the LoLMMRChecker bot. Have fun exploring the skill levels of your fellow summoners!
