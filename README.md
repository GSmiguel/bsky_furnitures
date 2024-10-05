BlueSky Furniture Bot

This is a simple project that aims to integrate various APIs to create a bot that makes periodic posts with furniture-related images on BlueSky's platform (https://bsky.app/profile/furnitures.bsky.social).

The basic_script.py file contains the BlueSky login and password information (which are kept hidden through the .env file) and outlines how the images will be selected from the Pexels API.

The main.yml file was created using GitHub Actions, setting up a cron job to run the basic_script.py periodically.
