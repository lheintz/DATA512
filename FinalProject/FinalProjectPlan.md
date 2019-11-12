# <center> A5 Final Project Plan </center>
<center> DATA 512 </center>
<center> Human Centered Data Science </center>
<center> Lauren Heintz  </center>
<center> 11/14/2019 </center>
 
 ----

## Introduction

While I am studying part time to become a data scientist, my full-time job is at The Boeing Company. There has recently been a lot of news and media on Boeing surrounding the 737Max crashes. This brings attention to air travel and the safety of air travel. I believe more people than ever are interested in learning more about air travel safety and the history air travel safety. I also believe there is a lot of confusion and misleading of late, in part due to the media attention on the aviation industry. 

For a naive reader, it may be hard to make sense of all this aerospace jargon being thrown around in the media. Busy travelers who do not work at an aviation company will want to skip straight to the facts on air travel safety. 

I hope that I can provide some scientific, fact-based, data-based information to these busy American travelers. Hopefully my research can provide conclusions that any adult reader can understand and find value in. This analysis will also strive to provide a historical lens from which to view the recent events. I will focus on United States air travel specifically.

In my analysis I plan to investigate the trends in aviation accidents and fatalies over time. I will also look at tangible factors that all readers can understand and use descriptive statistics and visualizations to bring light to patterns if they exist. 

----


## Research Question

1. How has the safety of commercial* air travel in the United States changed over the past ~30 years?

* 1 a. How has the number of accidents/fatalies in the United States changed over the past ~30 years? 
* 1 b. How has the ratio of accidents/fatalies per annual miles flown in the United States changed over the past ~30 years? 
* 1 c. How has the ratio of accidents/fatalies per annual flights hours  in the United States changed over the past ~30 years? 
* 1 d. How do the rates of accidents/fatalities vary between commercial* and all public and private flights?

2. What kinds of planes are responsible for the most accidents? 

3. How does the experience level of the pilots impact airplane crashes?

*'Commercial' is defined as a flight regulated under 14 CFR-121 - see background section for definition

------


## Background Research

Upon some google searching about the safety of flight, one article brings up some interesting statistics which immediately point to the overwhelming safety of air travel in comparison to other modes of transportation. **"There are a range of estimates out there, but based on its analysis of US Census data, it puts the odds of dying as a plane passenger at 1 in 205,552. That compares with odds of 1 in 4,050 for dying as a cyclist; 1 in 1,086 for drowning, and 1 in 102 for a car crash.**" ([SBS](https://www.sbs.com.au/news/how-safe-is-flying-here-s-what-the-statistics-say)) This article goes on to list some numbers about accidents, however, it only lists accidents from the US and Canada from 2013 to 2017. After that, the analysis looks at all countries, which my analysis does not. It appears to use the US National Safety Council data, not FAA data. 

Another top search result, a self help [blog](https://www.anxieties.com/flying-howsafe.php) for people with flying anxiety also compares air travel to other modes of travel. It states that **"In fact, based on this incredible safety record, if you did fly every day of your life, probability indicates that it would take you nineteen thousand years before you would succumb to a fatal accident. Nineteen thousand years!"** An additional comparison to the dangers of driving points out that **a sold-out 727 jet would have to crash every day of the week, with no survivors, to equal the highway deaths per year in this country."**

It points to outside sources for the following numbers:  
__DEATH BY: YOUR ODDS__  
Cardiovascular disease: 1 in 2  
Smoking (by/before age 35): 1 in 600  
Car trip, coast-to-coast: 1 in 14,000  
Bicycle accident: 1 in 88,000  
Tornado: 1 in 450,000  
Train, coast-to-coast: 1 in 1,000,000  
Lightning: 1 in 1.9 million  
Bee sting: 1 in 5.5 million  
U.S. commercial jet airline: 1 in 7 million  
[Sources: Natural History Museum of Los Angeles County, Massachusetts   Institute of Technology, University of California at Berkeley] 

These numbers vary significantly from the previous article, which could have to do with the date that it was written. It could also simply be because these odds are hard to estimate. Not only do you need to use an appropriate accident, you also need to appropriately estimate how often someone is flying or driving. For this very reason, I did not seek to incorporate other modes of transportation in to my analysis. The data was simply not available or accurate. In any case, it does not deep dive in to accidents, pilots, or any sort of time series analysis.

Finally, probably the most relevant result I found was a [bloomberg article](https://www.bloomberg.com/news/articles/2019-05-30/flying-has-become-more-dangerous-don-t-just-blame-boeing) warning that flying has become more dangerous recently. This article is touching on the same hot topic that I wish to address. While it does include one bar chart of total annual fatalities from 2010 to 2018, it does not include any other visuals. Even this visual is based on the world passenger airline fatality data, not the United States. It does not appear to be the same data set as mine, and the article quickly moves on to other factors in airplane safety such as demand for speed and cost cutting by airlines, as well as an increased burden of safety regulation.

I am excited say that despite the recent media craze, there really doesn't seem to be many data driven articles or publications recently to appeal to the general public in regards to the safety of air travel. This means that my research could really provide some benefit to the general public. It does not appear that my work is directly building off of anyone's previous. Since FAA data is widely available, I would not be surprised if someone had already done this analysis, however, it was not published and popularized anywhere that I found.



| Term   | Definition |
| ----- | --- |
| NTSB | National Transportation Safety Board |
| [14 CFR-121](https://www.govinfo.gov/app/details/CFR-2011-title14-vol3/CFR-2011-title14-vol3-part121/context) | Specification of Operating Requirements: Domestic, Flag, and Supplemental Operations, more than 10 passengers, scheduled service |
| [Domestic Operation](https://www.govinfo.gov/app/details/CFR-2011-title14-vol3/CFR-2011-title14-vol3-part121/context) | Departure and Arrival Airport both within US |
| [Flag Operation](https://www.govinfo.gov/app/details/CFR-2011-title14-vol3/CFR-2011-title14-vol3-part121/context) | Departure from US Airport, Arrival in non-US Airport |
| [Supplemental Operation](https://www.govinfo.gov/app/details/CFR-2011-title14-vol3/CFR-2011-title14-vol3-part121/context) | Departure and Arrival from US Airports, cargo or large charter |
| [Accident](data_raw/accidentsFatalitiesRates_airlines.csv) | An accident in these data sets means that an illegal act such as __suicide, sabotage, or terrorism__ was NOT responsible for the occurrence. For example, 9/11 2001 terrorism fatalies are excluded but available another data set. |
| [Accident, Major](data_raw/accidentsAccidentRates_scheduledPass.csv) | Major - an accident in which any of three conditions is met: 1) a Part 121 aircraft was destroyed, or 2) there were multiple fatalities, or 3) there was one fatality and a Part 121 aircraft was substantially damaged. |
| [Accident, Serious](data_raw/accidentsAccidentRates_scheduledPass.csv) | Serious - an accident in which at least one of two conditions is met: 1) there was one fatality without substantial damage to a Part 121 aircraft, 2) there was at least one serious injury and a Part 121 aircraft was substantially damaged. |
| [Accident, Injury](data_raw/accidentsAccidentRates_scheduledPass.csv) | Injury - a nonfatal accident with at least one serious injury and without substantial damage to a Part 121 aircraft. |
| [Accident, Damage](data_raw/accidentsAccidentRates_scheduledPass.csv) | Damage - an accident in which no person was killed or seriously injured, but in which any aircraft was substantially damaged. |

------

## Data


| Source | File Name |    Table Name    | Years | Data Source |
| ---- | ------ | ------------ | ------- | ----|
| 1 | faaAccidentIncidentDataSystem.csv | FAA Accident and Incident Data System (AIDS) | 1978 - 2015 | https://www.asias.faa.gov/apex/f?p=100:11:::NO::: |
| 2 | accidentsAccidentRates_scheduledPass.csv | Accidents and Accident Rates by NTSB Classification, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121 | 1983 - 2014| https://catalog.data.gov/dataset/accidents-and-accident-rates-by-ntsb-classification-1995-through-2014-for-u-s-air-carriers |
| 3 | accidentsFatalitiesRates_airlines.csv | Accidents, Fatalities, and Rates, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121, Scheduled and Nonscheduled Service (Airlines) | 1983 - 2014| https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-for-u-s-air-carriers-operating-under-14-c-dae36|
| 4 | accidentsFatalitiesRates_genAv.csv | Accidents, Fatalities, and Rates, 1995 through 2014, U.S. General Aviation | 1975 - 2014 | https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-u-s-general-aviation |


> There are multiple data sets that I plan to use in tandem to complete my analysis. The most detailed data set is the FAA Accident & Incident Data System - which contains a detailed record for every single accident and incident from ~1978 to ~2015 (with MM/DD/YYYY available for each) for any type of United States flight (private, commercial, scheduled, unschedule, cargo, passenger). Examples of the relevant fields of data available for each row item are: Local Event Date, Event City, Event State, Event Airport, Event Type, Aircraft Damage, Flight Phase, Aircraft Make, Aircraft Model, Aircraft Series, Operator, Primary Flight Type, Total Fatalities, Total Injuries, PIC Certificate Type, PIC Flight Time Total Hrs, PIC Flight Time Total Make-Model.   

> The other data sets are at an aggregate level and may be more useful for those less familiar with aviation terminology. The second and third data sets are for scheduled, passenger flights - so generally commercial airlines. The second source contains more details as to the severity of accidents and the third source contains more details as to the number of fatalities. They have several columns of redudant data though, so I will likely join these two data sets and eliminate the redudandant columns and keep all unique columns so that I have the maximum granularity for these two data sets. The second data sets contains the following fields: Year, Accidents: Major,Accidents: Serious, Accidents: Injury, Accidents: Damage, Aircraft hours flown (millions), Accidents per Million Hours Flown: Major, Accidents per Million Hours Flown: Serious, Accidents per Million Hours Flown: Injury, Accidents per Million Hours Flown: Damage. 

> The third data set contains the following fields:  Year, Accidents: All, Accidents, Fatal, Fatalities: Total, Fatalies: Aboard, Flight Hours, Miles Flown, Departures, Accidents ?: All, Accidents ?: Fatal, Accidents : All,  Accidents ?: Fatal, Accidents per 100,000 Departures: All, Accidents per 100,000 Departures: Fatal.

> The fourth data set is general aviation, so it includes private and personal flights, not just scheduled commercial passenger flights. Therefore it includes more types of planes, smaller planes, and more airports. That information is not detailed in this data set, but on a whole it represents way more flight hours and way more total accidents. It contains the fields: Year, Accidents: All, Accidents: Fatal, Fatalities: Total, Fatalities: Aboard, Flight Hours, Accidents per ?: All, Accidents per ?: Fatal 

> I did not come across any ethical concerns for using the data, as it is federally licensed and distributed - open for public consumption.  In fact, the largest data set is from the "ASIAS" project - Aviation Safety Information Analysis and Sharing. It appears the intention behind making this data available is to encourage transparency and analysis in the aviation industry.
     
-----

## Methodology

For each research question proposed, I will now explain my methodology for this analysis and presentation to the reader. 

1. How has the safety of commercial* air travel in the United States changed over the past ~30 years?

* 1 a. How has the number of accidents/fatalies in the United States changed over the past ~30 years? 

> For this, I will use data sources 2 & 3 to plot the aggregate totals either as a line or bar chart. Source 2 will be for accidents and source 3 will be for fatalities. I will make one plot for fatalities and one plot for accidents. For accidents, I will either plot multiple lines in different colors to denote the different types of accident totals, or used a stacked bar chart. For fatalities I will also use a line or bar chart. 

* 1 b. How has the ratio of accidents/fatalies per annual miles flown in the United States changed over the past ~30 years? 

> For these, I will again use tables 2 and 3 for accidents and fatalities respectively. Both of these tables contain rate information. I may address this question in several plots. First, plotting with a line or bar the gross miles flown per year. This will bring light to the huge spike in air travel in the past 30 years. After this, I will plot accidents and fatalities as a rate of miles flown per year. This will show that proportional to the increase in air travel over the years, the likelihood of being in a plane that gets in an accidents has gone down dramatically.

* 1 c. How has the ratio of accidents/fatalies per annual flights hours  in the United States changed over the past ~30 years? 

> For these, I will again use tables 2 and 3 for accidents and fatalities respectively. Both of these tables contain rate information. I may address this question in several plots. First, plotting with a line or bar the gross annual flight hours. This will bring light to the huge spike in air travel in the past 30 years. After this, I will plot accidents and fatalities as a rate of annual flight hours. This will show that proportional to the increase in air travel over the years, the likelihood of being in a plane that gets in an accidents has gone down dramatically.

* 1 d. How do the rates of accidents/fatalities vary between commercial* and all public and private flights?

> After addressing parts 1a-1c for just commercial* flights, I have data in table 4 contains the same accident, fatality, and rate data but instead for general aviation in the United States. I will use this to compare the relative safety of commercial flight vs general flight (include private and personal flights). I will choose just one metric - accidents per flight hour, and plot both the commercial and general aviation lines on the same plot in different colors.

2. What kinds of planes are responsible for the most accidents? 

> Finally, in looking at source 1, my most detailed data source, I can see more granular information for each accident. This contains the type of airplane for every data entry. To present to the reader what planes are responsible for the most crashes, I will create a pivot table that sums the number of accidents for each plane. Then, I will create a table for the reader that displays just the top 5 planes. Since I do not expect the reader to have a knowledge of all types of planes, I will either include an image or brief description of the plane.

3. How does the experience level of the pilots impact airplane crashes?

> A question a reader may ask if they are boarding a plane is - how experienced is my pilot? Data source 1, the detailed table, also contains a column with number of hours of experience of the Pilot In Control for most accidents. I will extract this column and create a histogram so that the reader can see the distribution of number of experience hours of pilots who have been in crashes, and observe for themselves if they think that number of hours could be a factor in safety.

-----

## License 
All data above information is federal government data, and therefore fits under the following free and open license: "U.S. Federal data available through [Data.gov](https://www.data.gov/privacy-policy#license) is offered free and without restriction. Data and content created by government employees within the scope of their employment are not subject to domestic copyright protection under 17 U.S.C. § 105." 

----

## Unknowns & Dependencies

The time series nature of the data used in this projects leads to some unknowns. Specifically because of my lack of experience working with time series data. Not all of the increments of time are the same for each data set (some are more granual than others). This presents a few unknowns on how the data will ultimately be compiled and used.

Additionally, the fact that there are 4 different data sets presents some challenges. They will need to be cleaned and joined together. Again, there are some dependencies on my ability to successfully and accurately join all this data in a limited amount of time (4 weeks). There may be some manual matching and comparison required. Realistically, I may be required to narrow down the scope of my data sets to the time range which all 4 data sets have in common. This is make my overall data set smaller in the end. In addition, I may be forced in some cases to change the granularity of the time series data in order to make my data clear and consistent.

Realistically, due to time constraints, it is possible the analysis may only consist of commercial flights, as I have more datasets which are applicable to this. Additionally, I imagine this is a more interesting topic to the general public, so if the data set is rich for airlines I may not analyze private flight data.

----

## Notes for Reuse

For these data sets, accidents which were caused by an illegal act such as __suicide, sabotage, or terrorism__ were NOT included in rate calculations. However, it is factored in to the overall accident and fatality numbers. For example, 9/11 2001 terrorism fatalies & accidents are included but do not affect the rate calculations for accidents per million miles flown or fatalies per million miles flown. Additionally, only those killed on board the planes in the 9/11 terrorist attack are included in the fataly numbers. Unless otherwise stated all fatalies are on board fatalies. Information on acts of __Suicide, Sabotage, or Terrorism on 14 CFR 121 Flights__ are available [elsewhere](https://catalog.data.gov/dataset/air-carrier-occurrences-involving-illegal-acts-sabotage-suicide-or-terrorism-1995-through-).   

There are some inconsistencies in the data as to which year is the last complete year of data. In general, all data stops at 2015 because the FAA releases a complete, verified set of data every 5 years (the next big release is 2020). Some data is incomplete for 2015 and some data is incomplete for 2014, so only data through 2013 will be utilized. 

Some of these data sets had headers and footers, or used two rows for the column label. These headers/footers were deleted and dual row column labels combined in to a single row prior to other preprocessing steps in the Jupyter notebook.

-------

## Other External References
[1] https://www.govinfo.gov/app/details/CFR-2011-title14-vol3/CFR-2011-title14-vol3-part121/context  
[2] https://catalog.data.gov/dataset/air-carrier-occurrences-involving-illegal-acts-sabotage-suicide-or-terrorism-1995-through-  
[3] https://www.sbs.com.au/news/how-safe-is-flying-here-s-what-the-statistics-say  
[4] https://www.anxieties.com/flying-howsafe.php  
[5] https://www.bloomberg.com/news/articles/2019-05-30/flying-has-become-more-dangerous-don-t-just-blame-boeing  
