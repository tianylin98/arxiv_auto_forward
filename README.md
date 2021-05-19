# axiv_auto_forward

Automatically gets Arxiv updates from predefined subject and send to your mailbox on a daily basis. It's for personal use, but anyone is welcom to use the code.
(This repo is still under construction.)

## Usage
1. Fork this repo to your own account;
2. Add the following Secrets to the repo (Settings -> Secrets):
  - SENDER_MAIL_USERNAME: The sender email address (currently only `outlook.com` is implemented);
  - SENDER_MAIL_PASSWORD: The sender email password;
  - RECEIVER_ADDR: addresses of receivers, separated with one space (e.g., `boredtylin@outlook.com tylin20@fudan.edu.cn` means I would like to send the mails to these two addresses).
  
3. Adapt the `config.json`. Here's an example:
  ```JSON
  {
    "subject": "cs.CL",
    "fields": ["id", "title", "name"],
    "highlights": ["Transformer", "Attention"]
  }
  ```
  The configuration means that I'm interested in `cs.CL` subject, and would like to highlight keywords "Transformer" and "Attention" in the titles.
  
4. Enable workflow from the Action in the repo. If you want to change the time schedule, please adapt the `cron` in the `.github/workflows/auto-forward.yml` file (For the time format, please refer to [official documentation](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule).

## Preview
If everything is set appropriately, the mail you receive would look like this:

![Preview of a sample email](https://github.com/boredtylin/arxiv_auto_forward/blob/main/preview.png)
