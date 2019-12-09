# Human Centered Data Science DATA 512 Final Project

Name: Lauren Heintz  
Date: 12/10/2019

# Purpose
While I am studying part time to become a data scientist, my full-time job is at The Boeing Company. There has recently been a lot of news and media on Boeing surrounding the 737Max crashes. This brings attention to air travel and the safety of air travel.  

The purpose of this project is to provide some scientific, fact-based, data-based information to these busy American travelers. Hopefully my research can provide conclusions that any adult reader can understand and find value in. This analysis will also strive to provide a historical lens from which to view the recent events. I will focus on United States air travel specifically.

In my analysis I plan to investigate the trends in aviation accidents and fatalities over time. I will also look at tangible factors that all readers can understand and use descriptive statistics and visualizations to bring light to patterns if they exist. 

I did not come across any ethical concerns in finding this aviation data or utilizing it. It is federally licensed and distributed - open for public consumption.  In fact, the largest data set is from the "ASIAS" project - Aviation Safety Information Analysis and Sharing. It appears the intention behind making this data available is to encourage transparency and analysis in the aviation industry.

There are several good reasons to perform a human centered data science investigation on the safety of air travel. The first reason is that with the recent media coverage surrounding the Boeing 737Max crashes, there is more journalism than ever on the topic. This journalism however is not always fact based or unbiased. The more media coverage there is, the more difficult it becomes to understand what is actually true. I believe it has gotten more and more difficult for American readers to sort through the information in front of them and determine what is subjective vs. objective. Many Americans are tired of this and want to get straight to the facts about air travel safety. I think my analysis could provide a means to do this.

Second, air travel has become increasingly popular over the past 3 decades, which we will see in my analysis below. Air travel is becoming more popular in the commercial sector specifically, as businesses depend on airplanes for international collaboration. On an individual level, recreational travel and tourism has gotten increasingly popular as prices for airplane tickets have dropped. This is a good reason to stop and take a moment to reflect on where air travel safety has been, and where it is headed as demand increases in the coming decade.

Finally, perhaps the most important reason for a human centered analysis on the topic: the laws of aerodynamics are complicated! So complicated that a graduate level degree in an aeronautical field is required to truly understand how planes work. For a naive reader not a part of the aerospace industry, it is hard to bridge this gap to truly understand the issues that the industry faces. This gap in understanding of how planes work leads to a gap in trust between the customers and the products. If customers don't understand what factors make a plane safe or not, how can they make an informed decision? How will they know whether or not to trust this flying metal bird in the sky? For the future of the aerospace industry, we must make products our customers have confidence in! This is why this type of work is even more important.

# Data 

| Source | File Name |    Table Name    | Years | Data Source |
| ---- | ------ | ------------ | ------- | ----|
| 1 | faaAccidentIncidentDataSystem.csv | FAA Accident and Incident Data System (AIDS) | 1978 - 2015 | https://www.asias.faa.gov/apex/f?p=100:11:::NO::: |
| 2 | accidentsAccidentRates_scheduledPass.csv | Accidents and Accident Rates by NTSB Classification, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121 | 1983 - 2014| https://catalog.data.gov/dataset/accidents-and-accident-rates-by-ntsb-classification-1995-through-2014-for-u-s-air-carriers |
| 3 | accidentsFatalitiesRates_airlines.csv | Accidents, Fatalities, and Rates, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121, Scheduled and Nonscheduled Service (Airlines) | 1983 - 2014| https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-for-u-s-air-carriers-operating-under-14-c-dae36|
| 4 | accidentsFatalitiesRates_genAv.csv | Accidents, Fatalities, and Rates, 1995 through 2014, U.S. General Aviation | 1975 - 2014 | https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-u-s-general-aviation |

### airline_aggregate.csv

| Variable Name | Data Type | 
| --- | --- |
|Year | Int |
| Illegal Act | Boolean identifier                               
| Flight Hours | Int |
| Miles Flown | Int |
| Departures | Int |
| Accidents, Major | Int |
| Accidents, Serious | Int |
| Accidents, Injury | Int |
| Accidents, Damage | Int |
| Accidents, All | Int |
| Accidents, Fatal | Int |
| Fatalities, Total | Int |
| Fatalities, Aboard | Int |
| Accidents per Million Hours Flown, Major | Float |
| Accidents per Million Hours Flown, Serious | Float |
| Accidents per Million Hours Flown, Injury | Float |
| Accidents per Million Hours Flown, Damage | Float |
| Accidents per 100,000 Flight Hours, All | Float |
| Accidents per 100,000 Flight Hours, Fatal | Float |
| Accidents per 1,000,000 Miles Flown, All | Float |
| Accidents per 1,000,000 Miles Flown, Fatal | Float |
| Accidents per 100,000 Departures, All | Float |
| Accidents per 100,000 Departures, Fatal | Float |

### genav_aggregate.csv

| Variable Name | Data Type | 
| --- | --- |
| Year | Int |
| Accidents, All | Int |
| Accidents, Fatal | Int |
| Fatalities, Total | Int |
| Fatalities, Aboard | Int |
| Flight Hours | Int |
| Accidents per 100,000 Flight Hour, All | Float |
| Accidents per 100,000 Flight Hour, Fatal | Float |

### faaAccidentIncidentDatabaseSystem.csv

## STILL NEED TO ADD DATA HERE

# Files

### Final Project

| Name | Type | Description |
| --- | --- | ---|
| data_raw | Folder | Contains all the data pre-processing stage |
| data_clean | Folder | Contains all the cleaned, post-processed data|
| src | Folder | Contains the analysis source code and final report Jupyter notebook - primary A7 deliverable. |
| `FinalProjectProposal.md` | File | A4 Deliverable |
| `FinalProjectPlan.md` | File | A5 Deliverable |
| `DATA 512 HCDS Final Presentation.pdf` | File | A6 Deliverable |
| `LICENSE.md` | File | License for project repo. |
| `README.md` | File | README for project repo. |

data_raw
> * accidentsAccidentRates_scheduledPass.csv
> * accidentsFatalitiesRates_airlines.csv
> * accidentsFatalitiesRates_genAv.csv
> * faaAccidentIncidentDataSystem.csv

data_clean
> * airline_aggregate.csv
> * genav_aggregate.csv

src
> * Aviation Analysis.ipynb
> * Aviation Analysis.html

results
> * B-727.jpg
> * Cessna172S.jpg
> * Cessna180.jpg
> * Cessna182.jpg
> * Cessna206.jpg
> * Cessna210.jpg
> * DC-3.jpg
> * DHC-6.jpg
> * M-20.jpg
> * PA-28.jpg
> * PIC_experience_hours.png
> * accidents_bars.png
> * accidents_lines.png
> * accidents_major_hours_lines.png
> * accidents_miles_lines.png
> * accidents_minor_hours_lines.png
> * departures.png
> * fatalities_by_make_model.csv
> * fatalities_hours_lines.png
> * fatalities_lines.png
> * fatalities_miles_lines.png
> * hours_bars.png
> * incidents_by_PIC_type.csv
> * incidents_by_make_model.csv
> * miles.png
> * public_private_accidents.png
> * public_private_accidents_hours.png
> * public_private_fatalities.png
> * public_private_fatalities_hours.png
> * public_private_hours.png	

# License

The license for this project can be found in the `LICENSE.md` file.
