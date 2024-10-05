BlueSky Furniture Bot

This is a simple project that aims to integrate various APIs to create a bot that makes periodic posts with furniture-related images on BlueSky's platform [https://bsky.app/profile/furnitures.bsky.social].
Features

    API Integration: Utilizes Pexels API to fetch random furniture images.
    Periodic Posting: Posts images to BlueSky at regular intervals.
    Environment Variables: Uses a .env file to store sensitive information securely.

Getting Started

    Clone the repository:

    bash

git clone https://github.com/yourusername/repository-name.git

Install the required packages:

bash

pip install -r requirements.txt

Create a .env file in the root directory and add your credentials:

plaintext

BLUESKY_EMAIL=your_email@example.com
BLUESKY_PASSWORD=your_password
PEXELS_API_KEY=your_pexels_api_key

Run the script locally to ensure it works:

bash

python basic_script.py

Set up a GitHub Action to run the script periodically (refer to the .github/workflows/your_workflow.yml file for configuration).
