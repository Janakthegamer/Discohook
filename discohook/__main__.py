""" Entry point to trigger webhook(s). """
import argparse
from client import Discohook


def main():
    parser = argparse.ArgumentParser(
        prog="discord_webhook", description="Trigger discord webhook(s)."
    )
    parser.add_argument(
        "-u", "--url", required=True, nargs="+", help="Webhook(s) url(s)",
    )
    parser.add_argument("-c", "--content", required=True, help="Message content")
    parser.add_argument(
        "--username", default=None, help="override the default username of the webhook"
    )
    parser.add_argument(
        "--avatar_url", default=None, help="override the default avatar of the webhook"
    )
    args = parser.parse_args()
    webhook = Discohook(
        url=args.url,
        content=args.content,
        username=args.username,
        avatar_url=args.avatar_url,
    )
    webhook.execute()


if __name__ == "__main__":
    main()
