from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='your webhook url', content='Webhook Message')
webhook.execute()
