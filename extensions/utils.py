from . import jalali
def persian_digits_converter(number):
    digits = {
        '0' : "۰",
        '1' : "۱",
        '2' : "۲",
        '3' : "۳",
        '4' : "۴",
        '5' : "۵",
        '6' : "۶",
        '7' : "۷",
        '8' : "۸",
        '9' : "۹",
    }
    for e,p in digits.items():
        number = number.replace(e, p)

    return number
    
def jalali_converter(time):
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد',
               'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    jtime = jalali.Gregorian(time.strftime('%Y-%m-%d')).persian_tuple()
    for i, month in enumerate(jmonths):
        if jtime[1] == i:
            output = f'{jtime[1]}-{month}-{jtime[0]} ساعت {time.strftime("%H")}:{time.strftime("%M")}'
            break
    return persian_digits_converter(output)
