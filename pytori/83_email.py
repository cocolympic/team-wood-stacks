from email.mime.text import MIMEText

msg = MIMEText("team-wood-stacks")
msg["Subject"] = "頑張るぞー"
msg["From"] = "me@example.com"
msg["To"] = "you@example.com"