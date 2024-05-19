# Internet Speed Twitter Bot

This Python script automates the process of checking your internet speed using Speedtest.net and tweeting at your provider if the speed falls below the promised rate. It utilizes Selenium for web automation and dotenv for environment variable management.

## Features
- Checks internet speed using Speedtest.net
- Tweets at your provider if the speed is below the promised rate
- Customizable promised download and upload speeds
- Easy configuration with dotenv

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file in the project directory and add your Twitter credentials:

   ```plaintext
   twitter_id=YOUR_TWITTER_EMAIL
   twitter_password=YOUR_TWITTER_PASSWORD
   ```

## Usage
1. Run the script `internet_speed_twitter_bot.py`.
2. Sit back and relax while the bot performs the speed test and tweets at your provider if necessary.

## Configuration
- Adjust the promised download and upload speeds in the script according to your internet plan.
- Customize the tweet message to your liking in the `tweet_at_provider()` method.

## Disclaimer
- Use this script responsibly and ensure compliance with Twitter's usage policy to avoid any penalties or restrictions.
