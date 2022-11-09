import pandas as pd


def answer_the_questions(print_data=True):
    data = pd.read_csv('/Users/NA20359743/Desktop/adult.data.csv')

    # 1  How many people of each race are represented in this dataset?

    race_count = data.race.value_counts().to_dict()

    # 2What is the average age of men?

    data_men = data[data["sex"] == "Male"]
    avg_men_age = round(data_men["age"].mean(),1)

    # 3 What is the percentage of people who have a Bachelor's degree?

    data_bachelors = data[data["education"] == "Bachelors"]
    bachelors_percentage = round( (len(data_bachelors) / len(data)) * 100 , 1)

    # 4  What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K

    advanced_education = data[data["education"].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_above_50K = advanced_education[advanced_education["salary"] == '>50K']
    perc_adv_education_above_50K = round( (len(advanced_education_above_50K) / len(advanced_education)) * 100 ,1)

    # 5  What percentage of people without advanced education make more than 50K?

    lower_education = data[data["education"].isin(['Bachelors', 'Masters', 'Doctorate']) == False]
    lower_education_above_50K = lower_education[lower_education["salary"] == '>50K']
    perc_low_education_above_50K = round( (len(lower_education_above_50K) / len(lower_education)) * 100 ,1)

    # 6  What is the minimum number of hours a person works per week?

    min_working_hours_per_week = data['hours-per-week'].min()

    # 7  What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

    people_work_min_hours = data[data['hours-per-week'] == min_working_hours_per_week]
    people_work_min_hours_above_50K = people_work_min_hours[people_work_min_hours['salary'] == '>50K']
    perc_people_min_work_above_50K = (len(people_work_min_hours_above_50K) / len(people_work_min_hours)) * 100

    # 8  What country has the highest percentage of people that earn >50K and what is that percentage?

    data_above_50K = data.loc[data['salary'] == '>50K', 'native-country']
    country_with_above_50K = data_above_50K.value_counts()
    total_country_people = data['native-country'].value_counts()
    count_percentage = (country_with_above_50K / total_country_people) * 100
    result = [count_percentage.sort_values(ascending=False).index[0],
              round(count_percentage.sort_values(ascending=False).max(), 1)]
    highest_earning_country = result[0]
    highest_earning_country_percentage = result[1]


    # 9  identify the most popular occupation for those who earn >50K in India.

    data_india_above_50K = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    most_pop_occup_india = data_india_above_50K['occupation'].value_counts().index[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", avg_men_age)
        print(f"Percentage with Bachelors degrees: {bachelors_percentage}%")
        print(f"Percentage with higher education that earn >50K: {perc_adv_education_above_50K}%")
        print(f"Percentage without higher education that earn >50K: {perc_low_education_above_50K}%")
        print(f"Min work time: {min_working_hours_per_week} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {perc_people_min_work_above_50K}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", most_pop_occup_india)

    return {
        'race_count': race_count,
        'average_age_men': avg_men_age,
        'bachelors_percentage': bachelors_percentage,
        'perc_adv_education_above_50K': perc_adv_education_above_50K,
        'perc_low_education_above_50K': perc_low_education_above_50K,
        'min_working_hours_per_week': min_working_hours_per_week,
        'perc_people_min_work_above_50K': perc_people_min_work_above_50K,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'most_pop_occup_india': most_pop_occup_india
    }

answer_the_questions()


