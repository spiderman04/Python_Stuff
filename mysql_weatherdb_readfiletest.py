"""
A simple text manipulation script to scan input files and split MBs
of lines into seperate files by State and County. The second part
is to create basic STATE tables in MySQL and lastly add the data.
"""

import os
import pyodbc

MYSQL_SCHEMA_NAME = 'weatherdb'
state_list = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
    'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
    'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
    'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
    'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
    'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
    'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
    'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

def parse_raw_datafiles():
    local_path = os.getcwd()
    print(local_path)

    header_names_once = False
    next_county = ""

    with open(local_path + '.\\..\\Data\\US_counties_weather_2020.csv', 'r') as f:
        for line in f:
            itemList = line.split(',')
            with open('.\\..\\Data\\a_file_header_names.txt', 'a') as f2:
                if not header_names_once:
                    for item in itemList:
                        f2.write(item + "\n")
                    header_names_once = True
            f2.close
            if itemList[0] == 'state':
                print(line)
                with open('.\\..\\Data\\a_file_header.txt', 'a') as f2:
                    f2.write(line)
                f2.close
            elif itemList[0] in state_list:
                state_name = itemList[0]
                with open('.\\..\\Data\\' + state_name + '_state_data.txt', 'a') as f2:
                    print("Debug...........state name is " + state_name)
                    f2.write(line)
                f2.close

                county_name = itemList[1]

                with open('.\\..\\Data\\' + state_name + '_county.txt', 'a') as f2:
                    if county_name != next_county:
                        print("Debug...........unique county name is " + county_name)
                        f2.write(county_name + "\n")
                        next_county = county_name
                f2.close

    f.close()

def create_state_tables():

    conn = pyodbc.connect("DSN=DSN_MYSQL_WEATHERDB", autocommmit=True)
    Cursor = conn.cursor()

    for item in state_list:
        print("Create base database table for ....." + str(item))

        sql_create = "create table if not exists `" + MYSQL_SCHEMA_NAME + "`." \
            + "`" + item.lower() + "` ( \
            id  int not null auto_increment, \
            county varchar(100), \
            state varchar(25), \
            temp_fahrenheit decimal(5,2), \
            temp_celsius decimal(5,2) as ((temp_fahrenheit - 32.0) / 1.8), \
            dt timestamp, \
            primary key (id)\
        );"

        Cursor.execute(sql_create)
        conn.commit()

    # close all connections
    Cursor.close()

def add_county_and_state():
    conn = pyodbc.connect("DSN=DSN_MYSQL_WEATHERDB", autocommmit=True)
    Cursor = conn.cursor()

    for item in state_list:
        print("Add county names for ....." + str(item))

        # read thru the county data file for all the names
        data_file = item + "_county.txt"
        with open( os.getcwd() + '.\\..\\Data\\' + data_file, 'r') as f:
            for county_name in f:
                if county_name != '\n':
                    print(county_name)

                sql_create = "insert into `" + MYSQL_SCHEMA_NAME + "`." \
                             + "`" + item.lower() + "` (county, state) values ('" \
                            + county_name.replace("'", "").replace("\n", "") \
                             + "','" + item + "');"

                Cursor.execute(sql_create)
                conn.commit()

    # close all connections
    Cursor.close()

def drop_tables():

    conn = pyodbc.connect("DSN=DSN_MYSQL_WEATHERDB", autocommmit=True)
    Cursor = conn.cursor()

    for item in state_list:
        print("Droping state table for ....." + str(item))
        sql_create = "drop table if exists `" + MYSQL_SCHEMA_NAME + "`." \
                     + "`" + item.lower() + "`;"

        Cursor.execute(sql_create)
        conn.commit()

    # close all connections
    Cursor.close()

def add_county_temp_and_date():
    conn = pyodbc.connect("DSN=DSN_MYSQL_WEATHERDB", autocommmit=True)
    Cursor = conn.cursor()

    for item in state_list:
        print("Add county names for ....." + str(item))

        # read thru the county data file for all the names
        data_file = item + "_state_data.txt"
        next_county = ""

        with (open( os.getcwd() + '.\\..\\Data\\' + data_file, 'r') as f):
            for line in f:
                col_data = line.split(',')

                if col_data[1] != next_county:
                    print("State=" + item + "  County=" + col_data[1] + "  Temp=" + col_data[11] + " Date=" + col_data[10])

                    sql_create = "update `" + MYSQL_SCHEMA_NAME + "`." \
                                 + "`" + item.lower() + "` set temp_fahrenheit='" + col_data[11]  \
                                 + "', dt= '" + col_data[10] + "' where county = '" \
                                + col_data[1].replace("'", "").replace("\n","") + "';"
                    next_county = col_data[1]

                Cursor.execute(sql_create)
                conn.commit()

    # close all connections
    Cursor.close()

def create_count_query_descending_by_county():
    with open('.\\..\\Data\\a_table_count_qry.txt', 'w') as f:
        for state_name in state_list:
            table_state_name = state_name.lower()
            if (state_name.lower() == 'alabama'):
                f.write("select a.* from ( \n")
                f.write("select '" + state_name + "' as 'State', count(*) as 'Table Count' from `" + table_state_name + "` union all \n")
            elif (state_name.lower() == 'wyoming'):
                f.write("select '" + state_name + "', count(*) from `" + table_state_name + "` \n")
                f.write(") a \norder by 2 desc;")
            else:
                f.write("select '" + state_name + "', count(*) from `" + table_state_name + "` union all\n")
    f.close()

def create_min_max_temp_query_by_state():
    with open('.\\..\\Data\\a_table_min_max_temp_qry.txt', 'w') as f:
        for state_name in state_list:
            table_state_name = state_name.lower()

            # do we quote the table name for MySql syntax
            if ((" " in table_state_name) == True):
                table_state_name = "`" + table_state_name + "`"
            else:
                table_state_name

            if (table_state_name == 'alabama'):
                f.write("select '" + state_name + "' as 'State', min(" + table_state_name +".temp_fahrenheit" \
                    + ") as 'Min Temp', max(" + table_state_name +".temp_fahrenheit" \
                        + ") as 'Max Temp' from `" + table_state_name + "` union all \n")
            elif (state_name.lower() == 'wyoming'):
                f.write("select '" + state_name + "', min(" + table_state_name + ".temp_fahrenheit" \
                        + ") as 'Min Temp', max(" + table_state_name + ".temp_fahrenheit" \
                            + ") as 'Max Temp' from " + table_state_name + " \n")
            else:
                f.write("select '" + state_name + "', min(" + table_state_name + ".temp_fahrenheit" \
                        + ") as 'Min Temp', max(" + table_state_name + ".temp_fahrenheit" \
                            + ") as 'Max Temp' from " + table_state_name + " union all \n")
    f.close()

def main():

    # start with clean db
    drop_tables()

    parse_raw_datafiles()
    create_state_tables()
    add_county_and_state()
    add_county_temp_and_date()
    create_count_query_descending_by_county()
    create_min_max_temp_query_by_state()




if __name__ == '__main__':
    main()
