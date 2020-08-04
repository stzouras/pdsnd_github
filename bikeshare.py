import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name: ")
    city=city.lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Enter valid city name: ")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month in text from january to june: ")
    month=month.lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('Enter a month within the specified range: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day in text: ")
    day=day.lower()
    while day not in ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('Enter a valid week day: ').lower()





    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])



    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1 
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]    

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month  = df['month'].mode()[0]
    print('most common month: ',most_common_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    most_common_day  = df['day'].mode()[0]
    print('Most common day of week: ',most_common_day)


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_start_hour  = df['start_hour'].mode()[0]
    print('Most common start hour ',most_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station  = df['Start Station'].mode()[0]
    print('Most commonly used start station ',most_start_station)
    
    # TO DO: display most commonly used end station
    most_end_station  = df['End Station'].mode()[0]
    print('Most commonly used end station: ',most_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combined_stations']  = df['Start Station'] + ' & ' + df['End Station']
    most_combined_stations  = df['combined_stations'].mode()[0]
    print('Most frequent combination of start station and end station trip: ',most_combined_stations)



    print(most_start_station,most_end_station,most_combined_stations)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    duration=df['End Time'].subtract(df['Start Time'])

    # TO DO: display total travel time
    total_travel=duration.sum()
    print('Total travel time: ',total_travel)
    # TO DO: display mean travel time
    mean_travel=duration.mean()
    print('Mean travel time: ',mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df.groupby('User Type')['User Type'].count()
    print('Counts of user types: ',user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts= df.groupby('Gender')['Gender'].count()
        print(gender_counts)
    except KeyError:
        print("No Gender column is available for Washington")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = min(df['Birth Year'])
        print(earliest_year)
        recent_year = max(df['Birth Year'])
        print(recent_year)
        common_year = df['start_hour'].mode()[0]
        print(common_year)
    except:
        print("There is no Birth Year data available for Washington city")
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def prompt_raw_data(df):
    """Displays blocks of five rows of the raw data."""    
    next_step = 'yes'
    number_of_steps=int(df.shape[0]/5)
    while next_step == 'yes':
        for i in range(number_of_steps):
            print(  df.iloc[ (i*5):(((i+1)*5))  ,])
            next_step = input('Do you want to continue yes/no? ')
            if next_step == 'no':
                break
        
        
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        prompt_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    
