import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
import scipy
from scipy import stats
import seaborn

print("successs")

data = pd.read_csv('./example/trip.csv')

print(len(data))
data.head()

# data = data.sort_values(by='birthyear')
# groupby_birthyear = data.groupby('birthyear').size()
# groupby_birthyear.plot.bar(
#     title='Distribution of birth years', figsize=(15, 4))

# data_mil = data[(data['birthyear'] >= 1977) & (data['birthyear'] <= 1994)]
# groupby_mil = data_mil.groupby('usertype').size()
# groupby_mil.plot.bar(title='Distribution of user types', figsize=(15, 4))

# # biẻu do kiẻm tra ai hoan thanh chuyen da ngoai theo gioi tinh, va tuoi
# groupby_birthyear_gender = data.groupby(['birthyear', 'gender'])[
#     'birthyear'].count().unstack('gender').fillna(0)
# groupby_birthyear_gender[['Male', 'Female', 'Other']].plot.bar(
#     title='Distribution of birth years by Gender', stacked=True, figsize=(15, 4))

# # biẻu do kiẻm tra ai hoan thanh chuyen da ngoai theo loai nguoi dung, va tuoi
# groupby_birthyear_user = data.groupby(['birthyear', 'usertype'])[
#     'birthyear'].count().unstack('usertype').fillna(0)
# groupby_birthyear_user['Member'].plot.bar(
#     title='Distribution of birth years by Usertype', stacked=True, figsize=(15, 4))
# 

tmp = data[data['usertype']=='Short-Term Pass Holder']['birthyear'].isnull().values.all()
print( "Kiem tra thanh vien ngan han co nhap nam sinh hay khong " , tmp)
tmp = data[data['usertype']=='Short-Term Pass Holder']['gender'].isnull().values.all()
print( "Kiem tra thanh vien ngan han co nhap gioi tinh hay khong " , tmp)


# Đầu tiên, chúng tôi đã chuyển đổi cột thời gian bắt đầu của khung dữ liệu thành một danh sách.
# Tiếp theo, chúng tôi đã chuyển đổi ngày chuỗi thành các đối tượng datetime python.
# Wethen đã chuyển đổi danh sách thành một đối tượng chuỗi và chuyển đổi ngày từ đối tượng datetime sang đối tượng ngày của gấu trúc.
# Các thành phần thời gian của năm, tháng, ngày và giờ được lấy từ danh sách với các đối tượng datetime.
# Biểu đồ thanh biểu thị sự phân phối thời gian chuyến đi theo thời gian hàng ngày
# 
List_ = list(data['starttime'])
List_ = [datetime.datetime.strptime(x, "%m/%d/%Y %H:%M") for x in List_]
data['starttime_mod'] = pd.Series(List_,index=data.index)
data['starttime_date'] = pd.Series([x.date() for x in List_],index=data.index)
data['starttime_year'] = pd.Series([x.year for x in List_],index=data.index)
data['starttime_month'] = pd.Series([x.month for x in List_],index=data.index)
data['starttime_day'] = pd.Series([x.day for x in List_],index=data.index)
data['starttime_hour'] = pd.Series([x.hour for x in List_],index=data.index)

data.groupby('starttime_date')['tripduration'].mean().plot.bar(title ='Distribution of Trip duration by date', figsize = (15,4))

plt.show()