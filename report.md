For my additional analysis, I decided to see if certain HCPCS codes are more common when the ICD code is I10 (Hypertension).

The results show that the HCPCS code with the highest frequency of I10 codes is 99221 which is for "Initial Hospital Inpatient or Observation Care" which makes sense as hypertension is something usually detected during a initial hospital visit

I tried to organize my code by following the steps and made it more structured by putting a header and spaces between each step.

Step 1: loads the data in and creates a new dataframe called df
Step 2: Explores the dataset and creates new variables based on 8 different medical codexes
Step 3: Analyzes the frequency of each unique value within each codex
Step 4: Handles missing data by identifying and filling in the missing values with a placeholder
Step 5: Summarizes the findings by printing the top 5 most common codes for each category

Challenges:
One challenge I faced was trying to print each column on a seperate line instead of having it all combined together and only seperated by a "|". It was very difficult to manually look through the list of codexes and pick the ones I wanted to use. I tried using "\n" to give spaces between each one but it didn't work.

Another challenge was finding the correct "sep" key. I originally though the seperator between each codex in the list was a "," but I kept receiving errors while making my codex variables and I wasn't sure why. I only realized that was the issue after several debugging tries.

The last challenge was just the formatting of the code and it was very tedious to make small changes to make it look nicer. Especially because I had to go back and fix previous parts of the code as well.


Reflection:
I think that this was a very interesting assignment and there can be a lot of interesting ways to find relationships and patterns amongst various codexes. I think this python code can be used for identifying the correlations with numbers and the next step would be to put this data on a graph for easier visualization. I think healthcare workers that look at this might be able to find overlapping issues and see if one diagnosis is correlated with a certain treatment or other condition. Maybe it can be used to identify shortcomings in care in a hospital or within a certain area, for example if there is a higher amount of admissions for a certain condition.
