#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[17]:


# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File path
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## Local Government Area Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average maths score 
# 
# * Calculate the average reading score
# 
# * Calculate the percentage of students with a passing maths score (50 or greater)
# 
# * Calculate the percentage of students with a passing reading score (50 or greater)
# 
# * Calculate the percentage of students who passed maths **and** reading (% Overall Passing)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[18]:


#Local Government Area Summary 
# Create dataframe
school_df = school_data_complete

# Calculate the total number of unique schools 
num_unique_schools = school_df['school_name'].nunique()
print("Number of Unique Schools:", num_unique_schools)

# Calculate the total number of students
num_student_ID = school_df['Student ID'].nunique()
print("Number of Students:", num_student_ID)

# Calculate the total budget
total_budget = sum(school_df['budget'].unique())
print("Total Budget:", total_budget)

# Calculate the average (mean) maths score
mean_maths = school_df['maths_score'].mean()
rounded_mean_maths = round(mean_maths,2)
print("Mean Maths Score:", rounded_mean_maths,"%")

# Calculate the average (mean) reading score
mean_reading = school_df['reading_score'].mean()
rounded_mean_reading = round(mean_reading,2)
print("Mean Reading Score:", rounded_mean_reading,"%")

# Calculate percentage of students who passed maths
maths_pass = school_df[school_df['maths_score'] >= 50]
maths_percentage_pass = (len(maths_pass)/ len(school_data_complete)) * 100
rounded_maths_percentage_pass = round(maths_percentage_pass, 2)
print("Maths pass rate:", rounded_maths_percentage_pass,"%")

# Calculate percentage of students who passed reading
reading_pass = school_df[school_df['reading_score'] >= 50]
reading_percentage_pass = (len(reading_pass)/ len(school_data_complete)) * 100
rounded_reading_percentage_pass = round(reading_percentage_pass, 2)
print("Reading pass rate:", rounded_reading_percentage_pass,"%")

# Set the passing hurdle
passing_hurdle = 50

# Calculate the percentage of students who passed both math and reading for all schools
overall_pass_rate = (len(school_data_complete[(school_data_complete['maths_score'] >= passing_hurdle) & (school_data_complete['reading_score'] >= passing_hurdle)]) / len(school_data_complete)) * 100
rounded_overall_pass_rate = round(overall_pass_rate,2)
print("Overall pass rate :", rounded_overall_pass_rate, "%")

#create a new DataFrame called area_summary
area_summary = pd.DataFrame({
    'Number of Unique Schools' : [num_unique_schools],
    'Number of Students' : [num_student_ID],
    'Total Budget' : [total_budget],
    'Mean Maths Score': [rounded_mean_maths],
    'Mean Reading Score': [rounded_mean_reading],
    'Maths Pass Rate (%)': [rounded_maths_percentage_pass],
    'Reading Pass Rate (%)': [rounded_reading_percentage_pass],
    'Overall Pass Rate (%)': [rounded_overall_pass_rate]
})

# Display DataFrame
(area_summary)


# ## School Summary

# * Create an overview table that summarises key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Maths Score
#   * Average Reading Score
#   * % Passing Maths
#   * % Passing Reading
#   * % Overall Passing (The percentage of students that passed maths **and** reading.)
#   
# * Create a dataframe to hold the above results

# In[19]:


# School Summary
# Create dataframe
per_school_summary = school_data_complete

# # pass hurdle
passing_hurdle = 50

per_school_summary = pd.DataFrame({
    'School Type': per_school_summary.groupby('school_name')['type'].max(),
    'Total Students': per_school_summary.groupby('school_name')['size'].unique().map(lambda x: x[0]),
    'Total School Budget': per_school_summary.groupby('school_name')['budget'].unique().map(lambda x: x[0]),
    'Per Student Budget': per_school_summary.groupby('school_name')['budget'].max() / school_data_complete.groupby('school_name')['size'].max(),
    'Average Maths Score': per_school_summary.groupby('school_name')['maths_score'].mean(),
    'Average Reading Score': per_school_summary.groupby('school_name')['reading_score'].mean(),
    '% Passing Math': (school_data_complete[school_data_complete['maths_score'] >= passing_hurdle]
                       .groupby('school_name')['Student ID'].count() / school_data_complete.groupby('school_name')['size'].unique().map(lambda x: x[0])) * 100,
    '% Passing Reading': (school_data_complete[school_data_complete['reading_score'] >= passing_hurdle]
                       .groupby('school_name')['Student ID'].count() / school_data_complete.groupby('school_name')['size'].unique().map(lambda x: x[0])) * 100,
    '% Overall pass': (school_data_complete[(school_data_complete['maths_score'] >= passing_hurdle) & (school_data_complete['reading_score'] >= passing_hurdle)]
                        .groupby('school_name')['Student ID'].count() / school_data_complete.groupby('school_name')['size'].unique().map(lambda x: x[0])) * 100
})

per_school_summary['Average Maths Score'] = per_school_summary['Average Maths Score'].map(lambda x: round(x,2))
per_school_summary['Average Reading Score'] = per_school_summary['Average Reading Score'].map(lambda x: round(x,2))
per_school_summary['% Passing Math'] = per_school_summary['% Passing Math'].map(lambda x: round(x,2))
per_school_summary['% Passing Reading'] = per_school_summary['% Passing Reading'].map(lambda x: round(x,2))
per_school_summary['% Overall pass'] = per_school_summary['% Overall pass'].map(lambda x: round(x,2))

# Display the per school summary DataFrame
(per_school_summary.head())


# ## Top Performing Schools (By % Overall Passing)

# * Sort and display the top five performing schools by % overall passing.

# In[20]:


# Sort top five performing schools by % overall passing
top_schools = per_school_summary.sort_values('% Overall pass', ascending=False)

# Reset index to display school name 
top_schools = top_schools.reset_index()

# top 5 schools
top_schools = top_schools[['school_name', '% Overall pass']].head(5)
(top_schools)


# ## Bottom Performing Schools (By % Overall Passing)

# * Sort and display the five worst-performing schools by % overall passing.

# In[5]:


# Sort bottom five performing schools by % overall passing
bottom_schools = per_school_summary.sort_values('% Overall pass', ascending=True)

# Reset index to display only school name 
bottom_schools = bottom_schools.reset_index()

# Bottom 5 schools
bottom_schools = bottom_schools[['school_name', '% Overall pass']].head(5)
(bottom_schools)


# ## Maths Scores by Year

# * Create a table that lists the average maths score for students of each year level (9, 10, 11, 12) at each school.
# 
#   * Create a pandas series for each year. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[21]:


# Create dataframe
math_scores_by_year = school_data_complete

# Create a pivot table 
maths_score_by_year = pd.pivot_table(math_scores_by_year, values='maths_score', index='school_name', columns='year', aggfunc='mean')

# Format the table 
maths_score_by_year.columns = [f'Year {col}' for col in maths_score_by_year.columns]
maths_score_by_year.reset_index(inplace=True)

# Display math score by year
maths_score_by_year


# ## Reading Score by Year

# * Perform the same operations as above for reading scores

# In[22]:


# Create dataframe
reading_scores_by_year = school_data_complete

# Create a pivot table 
reading_scores_by_year = pd.pivot_table(reading_scores_by_year, values='reading_score', index='school_name', columns='year', aggfunc='mean')

# Format the table 
reading_scores_by_year.columns = [f'Year {col}' for col in reading_scores_by_year.columns]
reading_scores_by_year.reset_index(inplace=True)

# Display results
reading_scores_by_year


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Maths Score
#   * Average Reading Score
#   * % Passing Maths
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[23]:


spending_summary = per_school_summary[['Per Student Budget','Average Maths Score','Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].copy()     
    
# Create bins in which to place values 
bins = [0, 584, 629, 644, 679]

# Create labels for these bins
group_labels = ["<$585", "$585-630", "$630-645", "$645-680"]

# Slice the data and place it into spending ranges bins

spending_summary['Spending Ranges (per Student)'] = pd.cut(spending_summary['Per Student Budget'], bins, labels=group_labels)

#Display 
spending_summary.groupby('Spending Ranges (per Student)')[['Average Maths Score','Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].mean()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[24]:


size_summary = per_school_summary[['Total Students', 'Average Maths Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].copy()

# Create bins in which to place values based upon school size
bins = [0, 999, 1999, float('inf')]  

# Create labels for these bins
group_labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Slice the data and place it into bins
size_summary['School Size'] = pd.cut(size_summary['Total Students'], bins, labels=group_labels)

# Group by 'School Size' and calculate the mean 
size_summary = size_summary.groupby('School Size')[['Average Maths Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].mean()

# Display
size_summary


# ## Scores by School Type

# * Perform the same operations as above, based on school type

# In[25]:


type_summary = per_school_summary[['School Type', 'Average Maths Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].copy()

# Group by 'School Type' 
type_summary_grouped = type_summary.groupby('School Type')[['Average Maths Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall pass']].mean()

# Display the grouped summary
type_summary_grouped


# In[ ]:




