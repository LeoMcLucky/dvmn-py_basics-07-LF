import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse

load_dotenv()

TG_TOKEN = os.getenv('TELEGRAM_TOKEN')


def reply(chat_id, text):
    time = parse(text)
    start_message_id = bot.send_message(chat_id, "Таймер запущен...")
    bot.create_countdown(time, notify_progress, author_id=chat_id,
                         message_id=start_message_id, var_rp=var_rp,
                         total=time)
    bot.create_timer(time, notify, author_id=chat_id)


def notify_progress(time, author_id, message_id, var_rp, total):
    progresbar = var_rp(total, time)
    print(progresbar)
    message_sec = "Осталось {t} секунд \n{p}".format(t=time, p=progresbar)
    bot.update_message(author_id, message_id, message_sec)


def notify(author_id):
    massage = "С Уважением - Время вышло"
    bot.send_message(author_id, massage)


def render_progressbar(total, iteration, prefix='', suffix='',
                       length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    var_rp = render_progressbar
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()
