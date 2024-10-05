# furnitures.bsky.social

This is a simple project that aims to integrate multiples APIs to create a bot that makes periodic posts with furniture-related images on[ bsky's platform](https://bsky.app/profile/furnitures.bsky.social).

The `basic_script.py` file contains the BlueSky login and password information (which are kept hidden through `secrets`) and outlines how the images will be selected from the Pexels API.

The `main.yml` file was created using GitHub Actions, setting up a cron job to run the `basic_script.py` periodically.
