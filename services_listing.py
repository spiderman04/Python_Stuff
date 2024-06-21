import os
import subprocess


if __name__ == '__main__':

    #os.system(f'net start {svc}')
    odd_list = []
    raw_service_names = []

    listing = os.popen("sc query type=all").read()

    with open('service_data.txt', 'w') as file:
        file.write(listing)
    file.close()

    with open("service_data.txt", "r") as file:
        my_list = file.readlines()
    file.close()

    # remove services' file from disk
    os.remove("service_data.txt")

    # parse thru the list looking for SERVICE_NAMES then the _#
    for line in my_list:
        if str(line).__contains__("SERVICE_NAME:"):

            raw_name = str(line).replace("SERVICE_NAME: ", '').replace('\n', '')
            raw_service_names.append(raw_name)

            if raw_name.__contains__("_"):
                #any(map(str.isdigit, s)) == True
                if  any(chr.isdigit() for chr in raw_name):

                    # save each unique service name and clean the \n and ' chars
                    cleaner = str(line).replace('\'', '').replace('\n', '')
                    odd_list.append(cleaner)


    # print service names only
    raw_service_names.sort()
    print("System Service Count: " + str(len(raw_service_names)))

    #debug
    #for item in raw_service_names:
        #print(item)

    #print("==============================")
    print("Odd Service Count: " + str(len(odd_list)))
    odd_list.sort()
    for item in odd_list:
        # user service name as simple batch script
        print("net stop " + item.replace("SERVICE_NAME: ", ''))