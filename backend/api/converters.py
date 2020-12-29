

#در یو ار ال ها می توانیم نوع دیتای دریافتی را خودمان نیز شخصی سازی کنیم
# کلاس زیر
class EncodeTokenPathConverter:

    regex='^[a-zA-Z0-9.]+$'

    #تابع زیر اگر نتواند تبدیل کند
    #ValueError
    #خواهد داد
    def to_python(self, value):
        # convert value to its corresponding python datatype
        return value

    def to_url(self, value):
        # convert value to str data
        return value
