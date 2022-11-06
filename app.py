import streamlit as st
import requests
def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()
	print(type(res))
	return res
def getCountyOption(items, target):
	optionList=list
	for item in items:
		name = items['cityname']
		# hint: 想辦法處理 item['cityName'] 的內容
		name.strip()
		if name not in optionList:	
			optionList.append(name)
	return optionList
def getSpecificBookstore(items, county):
	specificBookstoreList = []
	for item in items:
		name = item['cityName']
		if county not in name:
			continue
		specificBookstoreList.append(item)
	return specificBookstoreList
def getBookstoreInfo(items):
	expanderList = []
	for item in items:
		expander = st.expander(item['name'])        
		expander.image(item['representImage'])
		expander.metric('hitRate', item['hitRate'])
		expander.subheader('Introduction')
		expander.write(item['intro'])
		expander.subheader('Address')
		expander.write(item['Addres'])
		expander.subheader('Open Time')
		expander.write('Open Time')
		expander.subheader('email')
		# 用 expander.write 呈現書店的 Open Time
	expander.subheader('Email')
	# 用 expander.write 呈現書店的 Email
	# 將該 expander 放到 expanderList 中
def app():
	bookstoreList = getAllBookstore()
	countyOption = getCountyOption(bookstoreList)
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118)
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	specificbookstre=getSpecificBookstore(bookstoreList,county)
	num = len(specificbookstre)
	st.write(F'總共有[num]間書店')
if __name__ == '__main__':
    app()