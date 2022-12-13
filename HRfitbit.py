import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd

CLIENT_ID = '238RX8'
CLIENT_SECRET = 'dff37bf9cb0059dfc910129162e035ba'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)


oneDate = pd.datetime(year = , month = , day = )
oneDayData = auth2_client.intraday_time_series('activities/heart', oneDate, detail_level='1sec')
df= pd.DataFrame(oneDayData['activities-heart-intraday']["dataset"])

print(df)
df.to_csv('HRdata.csv')