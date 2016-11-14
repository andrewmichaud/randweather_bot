"""Main class to run randomweather_bot."""

import random
import time

import tweepy

import weather_gen
import send
import util

# Delay between tweets in seconds.
DELAY = 3600
DELAY_VARIATION = 600

if __name__ == "__main__":
    api = send.auth_and_get_api()

    LOG = util.set_up_logging()

    while True:
        LOG.info("Sending a weather tweet.")
        weather = weather_gen.produce_status()

        try:
            api.update_status(weather)

        except tweepy.TweepError as e:
            LOG.critical("A Tweepy error we don't know how to handle happened.")
            LOG.critical("Error reason: {}".format(e.reason))
            LOG.critical("Exiting.")
            break

        LOG.info("Sleeping for {} seconds.".format(DELAY))
        time.sleep(random.choice(range(DELAY-DELAY_VARIATION, DELAY+DELAY_VARIATION+1)))