from django import template
import datetime
import pytz

register = template.Library()

@register.filter(name='timesince_custom')
def timesince_custom(sincewhen):
    dif_days = (datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")) - sincewhen).days
    dif_seconds = (datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")) - sincewhen).seconds
    hours = int(dif_seconds/3600)
    minutes = int((dif_seconds - 3600 * hours)/60)
    seconds = int(dif_seconds - 3600 * hours - 60 * minutes)
    return str(dif_days) + " 天 " + str(hours) + " 小时 " + str(minutes) + " 分钟 " + str(seconds) + " 秒"

# skill_points_max 就是最大目标天数
@register.filter(name='skill_points')
def skill_points(sincewhen, skill_points_max):
    dif_days = float((datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")) - sincewhen).days)
    dif_seconds = (datetime.datetime.now(tz=pytz.timezone("Asia/Shanghai")) - sincewhen).seconds
    return float((dif_days + dif_seconds / 86400) / skill_points_max * 100)