# Overview

Nostr bot triggered by cron.

# Local Development

For local development see configuration in [.env](.env).

## Setup

### ENV

Inject ENV variables into your container or if running locally create a **.env** file like below:

```
PRIVATE_KEY_HEX=<private>
RELAYS=wss://nostr.mom,wss://relay.nostr.band,wss://relay.primal.net
PROFILE_DISPLAY_PIC_URL=https://i.imgur.com/vVsjW9D.jpeg
PROFILE_DISPLAY_NAME=Fancy Bot
PROFILE_ABOUT=Fancy Bot does things on a schedule
REDIS_BROKER_URL=redis://redis:6379/0
REDIS_BACKEND_URL=redis://redis:6379/0
CRON_HOURS=6
CRON_MINUTES=15
```


## Build

```
poetry install
```
## Generate Key

```
poetry run gen-key
```

*Note: set this key in the [.env](.env) file*

## Set Profile

Add profile information.

```
poetry run set-profile
```

## Run Bot

```
poetry run run-bot --debug
```

## Bot Container

### Build 

```
docker build -t <bot_name> .
```

### Run

```
docker run -d --name frogbot frogbot 
```

## Sheduled Composite

Run bot on a scheduled defined via **CRON_HOURS** and **CRON_MINUTES**.

### Build

```
docker-compose build --no-cache
```

### Run

```
docker-compose up -d  
```

### View Scheduled Tasks

```
localhost:5555
```

## Debug Container

```
docker exec frogbot /usr/local/bin/run-now.sh --debug
```