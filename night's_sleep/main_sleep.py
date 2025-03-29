import pandas as pd
sleep_health_data = pd.read_csv('sleep_health_data.csv')

#Find the occupation with the lowest sleep duration
lowest_sleep_duration = sleep_health_data.groupby('Occupation')['Sleep Duration'].mean()
lowest_sleep_duration = lowest_sleep_duration.sort_values(ascending=True)
lowest_sleep_quality_occ = lowest_sleep_duration.index[0]
print(f'Occupation with the lowest sleep duration is: {lowest_sleep_quality_occ}.')

#Find the occupation with the lowest sleep quality
lowest_sleep = sleep_health_data.groupby('Occupation')['Quality of Sleep'].mean()
lowest_sleep = lowest_sleep.sort_values(ascending=True)
lowest_sleep_occ = lowest_sleep.index[0]
print(f"Occupation with the lowest sleep quality is: {lowest_sleep_occ}.")

# Compare occupation with the least sleep to occupation with the lowest sleep quality
if lowest_sleep_occ == lowest_sleep_quality_occ:
  same_occ = True
else:
  same_occ = False

#Filter users in each BMI with insomnia
normal_insomnia = sleep_health_data[(sleep_health_data['Sleep Disorder'] == 'Insomnia') & (sleep_health_data['BMI Category'] == 'Normal')]
normal2 = sleep_health_data[(sleep_health_data["BMI Category"] == "Normal Weight") &
                  (sleep_health_data["Sleep Disorder"] == "Insomnia")]

obese_insomnia = sleep_health_data[(sleep_health_data['Sleep Disorder'] == 'Insomnia') & (sleep_health_data['BMI Category'] == 'Obese')]
overweight_insomnia = sleep_health_data[(sleep_health_data['Sleep Disorder'] == 'Insomnia') & (sleep_health_data['BMI Category'] == 'Overweight')]

#Calculate the ratio of app users in each BMI category have been diagnosed with Insomnia.
normal_total = len(sleep_health_data[sleep_health_data['BMI Category'] == 'Normal'])
normal_ratio = round(len(normal_insomnia) / normal_total, 2)

obese_total = len(sleep_health_data[sleep_health_data['BMI Category'] == 'Obese'])
obese_ratio = len(obese_insomnia) / obese_total
obese_ratio = round(obese_ratio, 2)

overweight_total = len(sleep_health_data[sleep_health_data['BMI Category'] == 'Overweight'])
overweight_ratio = len(overweight_insomnia) / overweight_total
overweight_ratio = round(overweight_ratio, 2)

print(f"Insomnia ratios in each BMI: "
      f"Normal: {normal_ratio}, Obese: {obese_ratio}, Overweight: {overweight_ratio}")

# Create dictionary to store the ratios for each BMI category
bmi_insomnia_ratios = {
    "Normal": normal_ratio,
    "Overweight": overweight_ratio,
    "Obese": obese_ratio
}