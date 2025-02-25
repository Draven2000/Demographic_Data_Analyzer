import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male']['age'].mean(), 1) #rounding to 1d.p

    # What is the percentage of people who have a Bachelor's degree?
    N_Bachelors = len(df.loc[df['education'] == 'Bachelors']['education']) #number of people with Bachelors
    N_Total = len(df) #Total number of people
    percentage_bachelors = round(N_Bachelors/N_Total * 100, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    N_higher = len(df.loc[
    ((df['education'] == 'Bachelors') 
    | (df['education'] == 'Masters') 
    | (df['education'] == 'Doctorate'))])

    N_lower = len(df) - N_higher
    higher_education = round(N_higher/N_Total * 100, 1)
    lower_education = round(N_lower/N_Total * 100, 1)

    # percentage with salary >50K
    N_higher_rich = len(df.loc[
    ((df['education'] == 'Bachelors') 
    | (df['education'] == 'Masters') 
    | (df['education'] == 'Doctorate'))
    & (df['salary'] == '>50K')]) 

    N_lower_rich = len(df.loc[
    ~((df['education'] == 'Bachelors') 
    | (df['education'] == 'Masters') 
    | (df['education'] == 'Doctorate'))
    & (df['salary'] == '>50K')]) 
    
    higher_education_rich = round(N_higher_rich / N_higher * 100, 1)
    lower_education_rich = round(N_lower_rich / N_lower * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    N_min_worker_rich = len(df.loc[
    (df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')]) 
    
    num_min_workers = len(df.loc[(df['hours-per-week'] == df['hours-per-week'].min())])

    rich_percentage = round(N_min_worker_rich/num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?

    Rich_by_country = df.loc[(df['salary'] == '>50K')]['native-country'].value_counts() # N of workers earing >50K by country
    N_by_country = df['native-country'].value_counts() # Total number of workers per country
    N_rich_by_country_percent = Rich_by_country/ N_by_country * 100 

    highest_earning_country = N_rich_by_country_percent.idxmax()
    highest_earning_country_percentage = round(N_rich_by_country_percent.max() , 1)

    # Identify the most popular occupation for those who earn >50K in India.

    India_50K = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    top_IN_occupation = India_50K['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
