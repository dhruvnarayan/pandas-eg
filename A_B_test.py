#import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click']=~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns='is_click',index='utm_source',values='user_id').reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True]/\
(clicks_pivot[False]+clicks_pivot[True])

experimental_group = ad_clicks.groupby(['is_click','experimental_group']).user_id.count().reset_index()
exp1 = experimental_group.pivot(columns='is_click',index='experimental_group',values='user_id')
exp1['percentage']=exp1[True]/(exp1[True]+exp1[False])

a_clicks = ad_clicks[ad_clicks.experimental_group=='A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group=='B'].reset_index()
a1 = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b1 = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()

aa=a1.pivot(columns='is_click',values='user_id',index='day')
bb=b1.pivot(columns='is_click',values='user_id',index='day')
aa['percentage']=aa[True]/(aa[True]+aa[False])
bb['percentage']=bb[True]/(bb[True]+bb[False])

print(aa)
print(bb)