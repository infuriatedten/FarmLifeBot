# FarmLifeBot

FarmLife Discord bot for the FarmLife FS community, built using discord.py.

## Features

- Greets new members when they join the server.
- **Prefix command**: `!hello [member]` sends a greeting to a user.
- **Slash command**: `/hello [member]` sends a greeting using an application command.

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/infuriatedten/FarmLifeBot.git
   cd FarmLifeBot
   ```
2. **Create a `.env` file** in the root directory with the following entries:
   ```env
   DISCORD_TOKEN=your_discord_token_here
   COMMAND_PREFIX=!
   ```
   - `COMMAND_PREFIX` defaults to `!` if omitted.
3. **Install dependencies**
   ```sh
   pip install -U discord.py python-dotenv
   ```
4. **Run the bot**
   ```sh
   python bot.py
   ```

## Configuration

- The bot reads environment variables from `.env`:
  - `DISCORD_TOKEN`: Your bot's authentication token.
  - `COMMAND_PREFIX`: Prefix for legacy commands (default is `!`).

## Database (Planned)

A database integration for user accounts and banking features is forthcoming. Current schema ideas:

- **Users**
  - `username`
  - `user_id`
- **Bank**

## Todo

- Implement database (MySQL/SQLite).
- Create user account commands.
- Add banking features.
- Log each command run to file and/or channel.
- Add error logging to file (e.g., `/var/log/bot/error.log`).
- Expand commands and cogs.

---
*This documentation will be updated as new features are added.*