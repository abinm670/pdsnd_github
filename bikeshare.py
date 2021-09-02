#Pro2
# Aug 11, 2021


import time
import pandas as pd
import numpy as np
import sys
def list_format(a_list):
    string_list = ["%i: %s" % (index, value) for index, value in enumerate(a_list)]
    return string_list

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = [key for key,value in CITY_DATA.items() ] 
all_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All']
all_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'All']

def get_user_input():

    main_message="\n".join(list_format(CITY_DATA))
    print('Hello! Let\'s explore some US bikeshare data! \n', main_message)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # select the city and convert the inputer to lower case and save the result the city
    city = input('Please select the city ').lower()
    
    # check if the city from the list
    while city  in cities:
    # if yes exit     
        break
    else:
    # if no loop unitll the user get the right input    
        while city  not in cities:
            city = input ("Choose only one \n Chicago, \t New York City, or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list="\n".join(list_format(all_month))
    # same as the above
    while True: 
        print('\n In Which Month.. \n ',month_list)
        month = input().capitalize()
        if month in all_month:
            break
        else:
            print('Try Again\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nIn Which day would you like.\n')
   
    # same as the above
    day_list="\n".join(list_format(all_days))
    while True:
        print('In which Day .. \n ', day_list)
        day = input().capitalize()
        if day in all_days:
            break
         
        else:
            print('Try Again! \n')
            
    print('-'*401)
    
    # At the end return the user input
    return city,month,day



def load_data(city, month, day):

   # load the data
   df = pd.read_csv(CITY_DATA[city])
    
   #disply the row data
   x=5
   answer= input('\n would you like to see row data? Yes or No \n').lower()
   while answer == 'yes':
    print('why', df.iloc[:x,:])
    x+=5
    answer= input('\n would you like to see more row data? Yes or No \n').lower()
   

   
   # create a new column and get the data time only 
   df['Start Time'] = pd.to_datetime(df['Start Time'])
   
   
   df['month'] = df['Start Time'].dt.month
   
   df['day'] = df['Start Time'].dt.day_name()
   
       

   if month != 'All':
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) +1


        df=df[df['month']==month]
   if day !='All':
        df=df[df['day']== day.title()]

   return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month !\n', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe most common day of week !\n', df['day'].mode()[0])

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('\nThe most common start hour\n',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_st = df['Start Station'].mode()[0]
    print('\nMost commonly used start station\n ', start_st)
    # TO DO: display most commonly used end station
    end_st = df['End Station'].mode()[0]
    print('\nMost commonly used end station\n ', end_st)    
    df['frequent_combination'] = df['Start Station'] +'\n___\n' +df['End Station']
    # TO DO: display most frequent combination of start station and end station trip
    print('\ndisplay most frequent combination of start station and end station trip\n',df['frequent_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    

    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    print('total traval time',trip_sum)
    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print('mean traval time',trip_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users= df['User Type'].value_counts()
    print('counts of users\n', users)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of Genders\n', gender)
    except:
        print("\nwe are Sorry ..The Washington city doesn't have data for gender\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       earliest =  df['Birth Year'].min()
       most_recent = df['Birth Year'].max()
       most_common = df['Birth Year'].mode()[0]
       print('\nEarliest year of birth {} \nMost recent year of birth {}\nMost common year of birth {}'.format(earliest,most_recent,most_common))
    except:
        print("\nwe are Sorry ..The Washington city doesn't have the data for birth year\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month,day = get_user_input()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
