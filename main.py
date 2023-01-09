
import schedule
import time
import pandas as pd
import datetime
import requests
import config
def sendEmail(to,sub,message):
    print(f"Email to {to} sent with subject: {sub} and message {message}")
    return requests.post(
		"https://api.mailgun.net/v3/18ankitjha.software/messages",
		auth=("api", config.API_KEY),
		data={"from":"mailgun@18ankitjha.software",
			"to": [to],
			"subject": sub,
			"text": message})
    pass


# if __name__ == "__main__":
def __name__():
    df=pd.read_excel("data.xlsx")
    print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    
    writeInd=[]
    for index,item in df.iterrows():
        print(index,item['Birthday'])
        bday=item['Birthday'].strftime("%d-%m")
        YearNow=datetime.datetime.now().strftime("%Y")
        if(today==bday) and YearNow not in str(item['Year']):
            print(sendEmail(item['Email'],"Happy Birthday from Ankit Jha","Happy Birthday 🥳🎉 "+item['Name'] +".May you get all the happiness 😊 in the world.Congratulations 🎉on being even more experienced. I’m not sure what you learned this year, but every experience transforms us into the people we are today. Happy birthday once again!. I Hope you have a wonderful day and a great year ahead."))
            writeInd.append(index)
    
    if(len(writeInd)>0):
        for i in writeInd:
            yr=df.loc[i,'Year']
            df.loc[i,'Year']=str(yr)+','+str(YearNow)
            df.to_excel('data.xlsx',index=False)

schedule.every().day.at("02:30").do(__name__)

while True:
    # print("Waiting for the mail to be sent")
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    schedule.run_pending()
    time.sleep(30)
    

