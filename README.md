# axiv_auto_forward

Automatically gets Arxiv updates from predefined subject and send to your mailbox on a daily basis. Plz feel free to use the code and report any issue.

## Usage
1. Fork this repo to your own account.
2. Add the following Secrets to the repo (Settings -> Secrets):
  - SENDER_MAIL_USERNAME: The sender email address (currently only `outlook.com` is implemented);
  - SENDER_MAIL_PASSWORD: The sender email password;
  - RECEIVER_ADDR: addresses of receivers, separated with one space (e.g., `boredtylin@outlook.com tylin20@fudan.edu.cn`).
  
3. Adapt the `config.json`. Here's an example:
  ```JSON
  {
    "subject": "cs.CL",
    "highlights": ["Transformer", "Attention"]
  }
  ```
  The configuration means that I'm interested in `cs.CL` subject, and would like to highlight keywords "Transformer" and "Attention" in the titles.
  
4. Enable workflow from the Action in the repo. If you want to change the time schedule, please adapt the `cron` in the `.github/workflows/auto-forward.yml` file (For the time format, please refer to [official documentation](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule)).

# 中文说明
自动从预设的subject下获取Arxiv更新，并每天讲内容发送到你的邮箱。欢迎使用和反馈问题。

### 使用说明
1. 将本仓库fork到你自己的账号。
2. 在仓库设置里添加如下secrets (Settings -> Secrets)：
  - SENDER_MAIL_USERNAME: 发件人邮箱(我只实现了`outlook.com`，欢迎自行修改端口和发件服务器);
  - SENDER_MAIL_PASSWORD: 发件人邮箱密码;
  - RECEIVER_ADDR: 收件人，用空格隔开 (e.g., `boredtylin@outlook.com tylin20@fudan.edu.cn`).

3. 修改`config.json`文件，这里提供一个例子：
  ```JSON
  {
    "subject": "cs.CL",
    "highlights": ["Transformer", "Attention"]
  }
  ```
  这个文件表示我需要接收cs.CL主题下的更新，并且希望在文章标题中高亮"Transformer"和"Attention"这两个词汇。
4. 在Action中启用本仓库中的workflow。如果需要修改刷新时间，请修改`.github/workflows/auto-forward.yml`中的`cron`字段（格式请参阅 [Github官方说明](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule)）
