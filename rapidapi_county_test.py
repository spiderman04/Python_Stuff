import http.client


def main():

    conn = http.client.HTTPSConnection("us-counties.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "18ae564d71msh5055473c3b50945p18d71Z",
        'X-RapidAPI-Host': "us-counties.p.rapidapi.com"
    }

    conn.request("GET", "/states", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data_list = data.decode('utf-8')

    print("Raw Data:\n" + data_list)

    with open('states.txt' ,'w') as f:
        f.write("State Listing from County API\n")
        f.write("=============================\n")
    f.close()

    data_list = []
    data_list.append(data.decode("utf-8"))

    with open('states.txt', 'a') as f:
        # loop thru each dictionary item in returned message
        for itemDict in data_list:
            f.write(itemDict)

            # loop thru key/val pair looking for specific items
            #for k, v in itemDict.items():
              #if (k == 'name' or k == 'abbreviation' or k == 'capital' or k == 'population'):
                    #f.write(str(k) + "=" + str(v) + ",")
            print()

    f.close()



    # EXAMPLE API #2
    conn = http.client.HTTPSConnection("dark-sky.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "18ae564d71msh5055473c3b50945p18d71Z",
        'X-RapidAPI-Host': "dark-sky.p.rapidapi.com"
    }

    conn.request("GET", "/37.774929,-122.419418,2019-02-20", headers=headers)

    res = conn.getresponse()
    data = res.read()

    with open('states.txt', 'a') as f:
        f.write(data.decode("utf-8"))

if __name__ == '__main__':
    main()