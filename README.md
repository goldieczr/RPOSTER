# INTRODUCTION
RPOSTER is a simple python bot designed to take one your post and repost it multiple subreddits as humanly as possible without the need of user interaction. Originally this bot was created to serve the NSFW niche, where adult models would post their pictures into tens to hundreds of subreddits on a daily basis, but it can be used in any other niche as well.
# HOW TO INSTALL

### Google Chrome

1. Install any version of [Google Chrome](https://www.google.com/chrome/) you want.
2. Go to the '[About Google Chrome](chrome://settings/help)' section and remember the version you installed.

### Chrome driver

1. Go to [Chrome driver](https://chromedriver.chromium.org/downloads) install page and download the version that matches your Google Chrome version.
2. Unzip the 'chromedriver.exe' into the main folder.

### Python & requirements

1. Download the latest version of [Python](https://www.python.org/downloads/) and install it.
2. [Install pip](https://www.geeksforgeeks.org/how-to-install-pip-on-windows) and follow it up with the requirements: `pip install selenium` `pip install pyfiglet` `pip install pwinput`

### Initial setup

1. Run `setup.py`
2. Provide your reddit account's credentials. The bot will automatically save a session cookie which will be used to log into your account without the need of inputting credentials at every run.
3. Open `post.txt` and replace the first line with the title of your post and the second line with the link, exactly as in the example provided.
5. Open `subreddits.txt` and input your list of subreddits, one subreddit on each line, exactly as in the example provided.

# USAGE
Simply start `main.py` and let it do it's job.
The bot will log into your account using the cookie saved through setup.py and will start posting your post into subreddits, one at a time, at a random interval of 20-40 seconds

Because this bot is in a very early stage, currently it can only do 'LINK' posts. Many new features coming soon.

# DISCLAIMER
This piece of software was made purely for educational purposes. USE AT YOUR OWN RISK. Reddit's Terms of Service clearly states that any kind of botting can result in your account being disabled. We try to make this process as humanly as possible, but nothing is guaranteed.

NEVER share the saved cookie inside `cookie.ini`, it can be used by anyone to log into your account without the need of login credentials.
