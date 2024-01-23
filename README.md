# pandas-challenge
**Analysis Summary**

15 schools in a local government area maths and reading scores were analysed in this challenge for students ranging from year 9 - 12. 

The data set included government and independent schools. 

The schools varied in sizes, ranging from less than 1,000 students to up to 5,000.

The spending on each student also varied widely, ranging from less than $585 to $680.


**Conclusions or comparisons from the calculations**

1). Independent schools performed better across both math and reading scores (and hence overall passing grade). 

The average reading score for independent schools was 70.7 (compared with 69.7 for government schools).

The average math score for independent schools 71.4 (compared with 69.8 for government schools).

2). Despite spending on government schools being on average higher than independent schools, the performance of independent schools is higher. 

Independent schools sampled in the data set on average had fewer number of students. It is therefore a reasonable assertion that size of school has a more favourable impact on student performance than spending per student.

**Results Output**

**Local Government Area Summary**
![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/5c2d8251-9754-4a75-a53e-39b96ae88ca4)


**School Summary**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/e6003dc1-553f-4385-bbf3-030bbeeb230d)


**Top Performing Schools (By % Overall Passing)**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/20c74970-a735-41a6-b428-7d9d01e4a7a1)

**Bottom Performing Schools (By % Overall Passing)**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/7e167862-bda3-4acf-b0b2-fd2a1be2ada2)

**Math Score by year**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/c534902b-b558-4961-bfbd-30728db245ca)

**Reading Score by year**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/da5f21c3-385c-4af9-a8dd-dfe1c00dc6cc)


**Scores by school spending**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/1a992999-e01f-4bbb-b0ab-46e5cc15250a)

**Scores by School Size**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/b8970949-c922-4a72-a4ff-cf8146cc0d56)


**Scores by School Type**

![image](https://github.com/L-Tren/Data-assignment-week4-pandas-challenge/assets/150787223/ff6096fd-0aae-4fed-879b-ce1e6525075d)


**Citing code sources**

**Local Government Area Summary/
School Summary**


I used the following inclass activities as the foundation of my code:


UADEL-VIRT-DATA-PT-12-2023-U-LOLC04-Data-Analysis-Pandas2Activities06-Ins_GroupBy
UADEL-VIRT-DATA-PT-12-2023-U-LOLC04-Data-Analysis-Pandas2Activities07-Par_Census_GroupBy

Data Sources: University of Adelaide. (2023). UADEL-VIRT-DATA-PT-12-2023-U-LOLC. Git Repository. https://git.bootcampcontent.com/University-of-Adelaide/UADEL-VIRT-DATA-PT-12-2023-U-LOLC/-/tree/main/04-Data-Analysis-Pandas/2/Activities/06-Ins_GroupBy/Unsolved?ref_type=heads

University of Adelaide. (2023). UADEL-VIRT-DATA-PT-12-2023-U-LOLC. Git Repository. https://git.bootcampcontent.com/University-of-Adelaide/UADEL-VIRT-DATA-PT-12-2023-U-LOLC/-/tree/main/04-Data-Analysis-Pandas/2/Activities/07-Par_Census_GroupBy?ref_type=heads



I then scheduled a tutoring session with Justin to trouble shoot and debug as the figures I was getting were not reconciling to the dataset and the table was displaying figures in brackets. He helped me debug and showed me how to use the lambda function to remove the brackets. Justin also helped me use a 'passing hurdle' to calculate the pass rates (maths & reading) and overall pass rate.

**Top Performing Schools (By % Overall Passing)/
Bottom Performing Schools (By % Overall Passing)**

I used the following inclass activities as the foundation of my code:
UADEL-VIRT-DATA-PT-12-2023-U-LOLC04-Data-Analysis-Pandas2Activities08-Ins_Sorting


Data Source: Vermont Agency of Administration, Department of Taxes. Meals and Rooms Tax Statistics (2020 Multiple Periods Update, Calendar Year). https://tax.vermont.gov/data-and-statistics/mrt

I was able to leverage the code from lesson 2 activity 8 to use for the top performing and bottom performing schools. With the assistance of ChatGPT to debug, I was successful in developing.


**Maths Scores by Year/
Reading Score by Year**

I asked BCS assistance for help on Maths Score and Reading Score by year. I felt the answer I received was clunky, and wanted to use a pivot table concept to display the data (as this is how I would approach at my job).

I was able to complete this was the assistance of chatGPT.

_Code for creating a pivot table with average math scores by school and year.
OpenAI. (2024). ChatGPT (Jan 20 version) [Pivot table python coding]. https://chat.openai.com/chat


**Scores by School Spending/
Scores by School Size/
Scores by School Type**

I used the following class activity as my starter code: 


UADEL-VIRT-DATA-PT-12-2023-U-LOLC04-Data-Analysis-Pandas3Activities04-Stu_MovieRatings_Binning.


Source FiveThirtyEight (2015). https://github.com/fivethirtyeight/data/tree/master/fandango

Justin and I in our tutor session were able to leverage this and apply to the dataset to use the bins as required (school spending, school size, and school type).
