# -*- coding: utf-8 -*-
"""پاکسازی ستون حقوق از صفر تا صد .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ajFT3wseGHzR53_-OY6HUcnF8c9CtRZd
"""

from google.colab import files

uploaded = files.upload()

df = pd.read_csv('memo.csv')

df

df['Salary Estimate']  #اوشاخلار ما فقط فعلا با این ستون کار میکنیم . با بررسی متوجه میشیم که کلی چیز میز اضافه داره مثل علامت دلار یا کا یا نوشته گلسدور

def dollors_remover( a): #اینجا هر چی میخوایم پاک کنیم رو براش تابع تعریف میکنیم و در جای مناسب این تابع رو بر جا و ستون مورد نظر اعمال میکنیم
  a = a.replace('$', ' ') #الان اینجا این تابع میگه که چشمم دلار نبینه و جاشو خالی کن یعنی چیزی که چسبیده به عددم که آ  باشه رو پاک کن
  return a  # بعدش خود عدد رو بدون دلار برگردون

def k_remover(a):   #اینجا هم میگه کا رو پاک کن یه تابعی نوشتیم که اعمال بشه به هر ستونی هر چی کا میبینه رو پاک کنه
  a = a.replace('K' , ' ')
  return a

df['Salary Estimate'] = df['Salary Estimate'].apply(dollors_remover).apply(k_remover) #اینجا میگم دو تا تابعی که تعریف کردمو اپلای کن به ستون سالاری و برابر سالاری هم تازه قرار بده
 #اینکه اول دستور خود ستون رو مینویسی یعنی حجت بر دستور تمام یعنی تغییرات قطعی و تغییراتی که دادیم پایدار باشه و تمام

df['Salary Estimate']  #اینجا من یه خروجی میگیرم که ببینم که تغییراتم ماندگار و ثبت شده؟؟؟ میبینم !!! بلههه

df = df[df['Salary Estimate'] != '-1'] #اینجا باز خنزل پنزل داریم!! چیه؟ آفرین -۱ اینم با این دستور میگیم که هر ستونی که -۱ داره رو حذف کن چون ما حقوق -۱ نداریم و محاسبات ما رو میتونه به خطا بندازه

df  #باز یه خروجی میگیریم ... به به

df = df[~df['Salary Estimate'].str.contains('Per Hour')] #اینجا ما میگیم که نبینم در ستون حقوق عبارت روبه رو را . ستون حقوق رو نشون بده بدون عبارت روبه رو

df  #حالا یه خروجی دیگه میگیریم و میبینیم که به به تمیز شد
# یه نکته بگم میتونه هر چیزی رو در ستون کلین کنی اما من کد اضافه نمینویسم چیزی که چسبیده به عددم و منو تو فراخوانی یا اندکس عددم دچار مشکل کنه رو پاک میکنم
#پس نیازی نمیبینم گلسدور رو پاک کنم چون اطراف ععدم پاک شد

df.to_csv('my_dataframe.csv')   #اینجا اول از همه فایلم رو سیو میکنم چون از تغغیرات مطمینم و میخوام بمونه برام

df['Salary Estimate'] = df['Salary Estimate'].apply(splitter) # اینجا میام ستون حقوقم رو از قانون اسپلیت جدا میکنم و تبدیل به لیست میکنم خیلی مهمه تبدیل به لیست میکنم

df   #باز یه خروجی میگیرم و به به ...

def min_finder (a):  #اینجا من یه تابع تعریف میکنم که کمترین مقدار هر سلولم را بکش بیرون
  a = a[0]
  return(a)

df['Salary Estimate'].apply(min_finder) #اینجا هم میگم تابعی که تعریفش کردم رو در ستون حقوق اعمال کن
# میبینید که کمترین اعداد رو در هر سلول از ستون حقوق نشون داد

df['Min_salary'] = df['Salary Estimate'].apply(min_finder) #حالا اون کمترین مقدار رو ببر براش یه ستون جدید بساز به اسم مین سالاری

df.info()  #مشاهده میکیند یه ایفو گرفتم که حساب کار دستم بیاد میبینی اون پایین ستون شماره ۱۱

def max_finder(a): #مجدد میام یه تابع واسه بیشترین مقدار تعریف میکنم
  a = a[2] #حضار محترم به ایندکس ها توجه کن با توجه به جدول ایندکس صفر کمترین مقدار و ایندکس یک میشه اون خط تیره و ایندکس ۲ میشه ماکزیمم عدد
  return(a) #یه نکته ای رو هم بگم اگر لیست نمیکردی در همین مرحله ایندکس به چوخ میرفتی چون کامپیتوتر چیزی دیگه میخوند
  #اگر لیست نمیشد تو هر خروجی از مین یا ماکس همه خروجی خالی نشون میداد یعنی بدون عدد

df['Max_salary'] = df['Salary Estimate'].apply(max_finder) # اینجا هم میگم بیا واسه ماکزیمم اعداد یه ستون بساز

df.info() # سلاطین حالا یه خروجی میگیریم . میبینیم به به.. هر دو ستون در ستونهای ۱۱ و ۱۲ ظاهر شد

df.columns #برای اینکه سر تیتر ستونها رو مجدد ببینیم چه خبره ؟ آیا ستونها ایجاد شده یا نه؟؟؟ از این دستور هم میه برای رویت کردن افتخارات نیز استفاده کرد

df.shape #برای اینکه سطر و ستون رو به صورت عددی شناسایی کنی هم به این صورت میشه رویت کرد
# یه نکته بگم بچه ها میبینی که از ۵۸۹۲ سطر رسیدیم به ۵۵۰۰ سطر ! جا افتاد ؟ کلین کردن اینطوری. خنزل پنزل رو میریزیم دور

df.head(4) #حالا یه این ۴ خط اول هم رویت میکینیم .. بله

df['Min_salary'].astype(int) #نکته قابل توجه اینکه کامپیوتر چیزمیزای داخل ستون حقوق منو عد  نمیبینه یه مشت آبجکت میبینه یه اینفو هم قبلش بگیری و ببینی میفهمی
# اما الان من میخوام اعمال ریاضی روی عددام انجام بدم پسس این دمو دستگاهو تبدیل به اینتجر میکنم تا عمل ریاضی روش انجام بدم

df['Min_salary'] = df['Min_salary'].astype(int) #حالا که عدد شد فیکس میکنم با ستون که یعنی این کارای منو سیو کن این ستون و بمونه

df['Max_salary'].astype(int) #این ماکسیموم هم عین دستور مینیموم انجام میدیم

df['Max_salary'] = df['Max_salary'].astype(int)  #اینجا هم فیکس میکنیم

df.info()   #یه دیتا میگیرم دسته گلام    به به چه کردی.... میبینی ستون ۱۱ و ۱۲ در نوع تایپ شدن اینتجر

df['Average_salary'] = (df['Min_salary'] + df['Max_salary'])/2  #حالا میام یه ستون جدید میسازم به اسم میانگین یه دستورم میدم بهش و تمامم

df.info() # اینجا یک اینفو میگیریم و ستون ۱۳ رو هم مشاهده میکنم.. و... چه چه