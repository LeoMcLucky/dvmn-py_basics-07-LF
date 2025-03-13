import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def reply(chat_id, text, bot):
    time = parse(text)
    start_message_id = bot.send_message(chat_id, "Таймер запущен...")
    bot.create_countdown(time, notify_progress, author_id=chat_id,
                         message_id=start_message_id, total=time, bot=bot)
    bot.create_timer(time, notify, author_id=chat_id, bot=bot)


def render_progressbar(total, iteration, prefix='', suffix='',
                       length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(time, author_id, message_id, total, bot):
    progresbar = render_progressbar(total, time)
    message_sec = "Осталось {t} секунд \n{p}".format(t=time, p=progresbar)
    bot.update_message(author_id, message_id, message_sec)


def notify(author_id, bot):
    massage = "С Уважением - Время вышло"
    bot.send_message(author_id, massage)


def main():
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_TOKEN')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
