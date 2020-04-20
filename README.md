# monitor-semdex
Python script to monitor a specific stock from the Stock Exchange of Mauritius and notify via a Telegram bot if there is any changes.

## Setup

Clone this repo first
```bash
git clone https://github.com/reallyaditya/monitor-semdex.git
```

### Getting IDs and Tokens

#### Telegram

- Create a Telegram bot using [Botfather]. (https://core.telegram.org/bots#6-botfather)
- Note down the bot token which will look like this `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`.
- Test the bot in the Telegram app to start a chat and get the Chat ID.
- Use this [Telegram Bot] to get the Chat ID. (https://telegram.me/myidbot)

#### SEMDEX ID

- Go to the [SEMDEX Homepage] and select the desired company. (https://www.stockexchangeofmauritius.com/)
- From the URL only copy the last part which contains the SEMDEX ID, e.g. For the URL of ABC BANKING CORPORATION LIMITED `https://www.stockexchangeofmauritius.com/products-market-data/equities-board/interactive-charting-dem?company=ABCB.I0000` the SEMDEX ID is `ABCB.I0000`. 

### Configuring the Script

- Open the `config.json` file and edit it out with the respective information (Telegram Chat ID and Bot Token, SEMDEX ID).

### Executing Script

- Run the script with the following command.

```bash
python3 monitor.py
```

- To continously monitor a SEMDEX stock, add the script as a Cron Job or to systemd
