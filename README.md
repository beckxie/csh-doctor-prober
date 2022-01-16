# csh-doctor-prober

> This tool periodically accesses [CSH's website], and you can receive Telegram notifications when having available places.

## Why I did this project

> I just want to make an appointment with a CSH's doctor who is famous, but all available places have been taken...ALWAYS!

## Prerequisites

- Python3
- chromedriver

## Installation

- Install packages with pip3 and [requirements.txt]
  
  ```bash
  pip3 install -r requirements.txt
  ```

- Download [chromedriver], and put it to `/usr/bin`, that will be `/usr/bin/chromedriver`.

## Usage

1. copy the example environment file that is your `.env` file: `cp .env.example .env`
2. edit `.env`
   1. `telegram_token`: your telegram bot token.
   2. `telegram_chat`: your telegram chat ID.
   3. `label_doctor_first_name`: The element ID of CSH's doctor first name on the [CSH's website].
   4. `label_doctor_name`: The element ID of CSH's doctor name on the [CSH's website].
   5. `label_doctor_division`: The element ID of CSH's doctor division on the [CSH's website].

3. execute and waiting: `python3 csh.py`

## License

This project is licensed under the MIT License - see the [LICENSE] file for details

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fbeckxie%2Fcsh-doctor-prober.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fbeckxie%2Fcsh-doctor-prober?ref=badge_large)

[requirements.txt]:./requirements.txt
[CSH's website]:https://sysint.csh.org.tw/Register/DoctorClinic.aspx
[chromedriver]:https://chromedriver.chromium.org/downloads
[LICENSE]: ./LICENSE
