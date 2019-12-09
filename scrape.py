from bs4 import BeautifulSoup
import requests
import csv



def get_data():
    soup = BeautifulSoup(open("/Volumes/Others/Downloads/test.htm"),'lxml') # path to html page 
    card_list=soup.find_all('li')
    result = []
    for card in card_list:
        url=card.a.text
        Description=card.strong.text
        result.append((url, Description))
    
    return result


def store_data(data):
    print('Saving result.csv')
    file = open('result.csv', 'w')
    writer = csv.writer(file, ['sl','url', 'Description'])
    for resl in data:
        writer.writerow([resl[0], resl[1]])
    file.close()


def main():
    data = get_data()
    store_data(data)


if __name__ == '__main__':
    main()