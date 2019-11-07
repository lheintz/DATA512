# <center> A4 Final Project Proposal </center>
<center> DATA 512 </center>
<center> Human Centered Data Science </center>
<center> Lauren Heintz  </center>
<center> 11/7/2019 </center>
 
 ----

## Motivation

While I am studying part time to become a data scientist, my full-time job is at The Boeing Company. There has recently been a lot of news and media on Boeing surrounding the 737Max crashes. This brings attention to air travel and the safety of air travel. I believe more people than ever are interested in learning more about air travel safety and the history air travel safety. I hope that I can provide some scientific, fact-based, data-based information and conclusions that a niave reader can understand and find value in. I will focus on United States air travel specifically.

I hope to learn about the trends in aviation accidents and fatalies over time. I hope to learn more about correlative factors to relative safety of a flight. I also hope to learn more about the differences in accident and fatality rates between commercial and private aviation in the United States.

----

## Data

> There are multiple data sets that I plan to use in tandem to complete my analysis. The most detailed data set is the FAA Accident & Incident Data System - which contains a detailed record for every single accident and incident from ~1978 to ~2015 (with MM/DD/YYYY available for each) for any type of United States flight (private, commercial, scheduled, unschedule, cargo, passenger). Examples of the relevant fields of data available for each row item are: Local Event Date, Event City, Event State, Event Airport, Event Type, Aircraft Damage, Flight Phase, Aircraft Make, Aircraft Model, Aircraft Series, Operator, Primary Flight Type, Total Fatalities, Total Injuries, PIC Certificate Type, PIC Flight Time Total Hrs, PIC Flight Time Total Make-Model.   

> The other data sets are at an aggregate level and may be more useful for those less familiar with aviation terminology. The second and third data sets are for scheduled, passenger flights - so generally commercial airlines. The second source contains more details as to the severity of accidents and the third source contains more details as to the number of fatalities. They have several columns of redudant data though, so I will likely join these two data sets and eliminate the redudandant columns and keep all unique columns so that I have the maximum granularity for these two data sets. The second data sets contains the following fields: Year, Accidents: Major,Accidents: Serious, Accidents: Injury, Accidents: Damage, Aircraft hours flown (millions), Accidents per Million Hours Flown: Major, Accidents per Million Hours Flown: Serious, Accidents per Million Hours Flown: Injury, Accidents per Million Hours Flown: Damage. 

> The third data set contains the following fields:  Year, Accidents: All, Accidents, Fatal, Fatalities: Total, Fatalies: Aboard, Flight Hours, Miles Flown, Departures, Accidents ?: All, Accidents ?: Fatal, Accidents : All,  Accidents ?: Fatal, Accidents per 100,000 Departures: All, Accidents per 100,000 Departures: Fatal.

> The fourth data set is general aviation, so it includes private and personal flights, not just scheduled commercial passenger flights. Therefore it includes more types of planes, smaller planes, and more airports. That information is not detailed in this data set, but on a whole it represents way more flight hours and way more total accidents. It contains the fields: Year, Accidents: All, Accidents: Fatal, Fatalities: Total, Fatalities: Aboard, Flight Hours, Accidents per ?: All, Accidents per ?: Fatal 

> I did not come across any ethical concerns for using the data, as it is federally licensed and distributed - open for public consumption.  In fact, the largest data set is from the "ASIAS" project - Aviation Safety Information Analysis and Sharing. It appears the intention behind making this data available is to encourage transparency and analysis in the aviation industry.
     
      

| Source | File Name |    Table Name    | Years | Data Source |
| ---- | ------ | ------------ | ------- | ----|
| 1 | faaAccidentIncidentDataSystem.csv | FAA Accident and Incident Data System (AIDS) | 1978 - 2015 | https://www.asias.faa.gov/apex/f?p=100:11:::NO::: |
| 2 | accidentsAccidentRates_scheduledPass.csv | Accidents and Accident Rates by NTSB Classification, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121 | 1983 - 2014| https://catalog.data.gov/dataset/accidents-and-accident-rates-by-ntsb-classification-1995-through-2014-for-u-s-air-carriers |
| 3 | accidentsFatalitiesRates_airlines.csv | Accidents, Fatalities, and Rates, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121, Scheduled and Nonscheduled Service (Airlines) | 1983 - 2014| https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-for-u-s-air-carriers-operating-under-14-c-dae36|
| 4 | accidentsFatalitiesRates_genAv.csv | Accidents, Fatalities, and Rates, 1995 through 2014, U.S. General Aviation | 1975 - 2014 | https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-u-s-general-aviation |


## License 
> All data above information is federal government data, and therefore fits under the following free and open license: "U.S. Federal data available through [Data.gov](https://www.data.gov/privacy-policy#license) is offered free and without restriction. Data and content created by government employees within the scope of their employment are not subject to domestic copyright protection under 17 U.S.C. § 105." 

----

## Unknowns & Dependencies

The time series nature of the data used in this projects leads to some unknowns. Specifically because of my lack of experience working with time series data. Not all of the increments of time are the same for each data set (some are more granual than others). This presents a few unknowns on how the data will ultimately be compiled and used.

Additionally, the fact that there are 4 different data sets presents some challenges. They will need to be cleaned and joined together. Again, there are some dependencies on my ability to successfully and accurately join all this data in a limited amount of time (4 weeks). There may be some manual matching and comparison required. Realistically, I may be required to narrow down the scope of my data sets to the time range which all 4 data sets have in common. This is make my overall data set smaller in the end. In addition, I may be forced in some cases to change the granularity of the time series data in order to make my data clear and consistent.

Realistically, due to time constraints, it is possible the analysis may only consist of commercial flights, as I have more datasets which are applicable to this. Additionally, I imagine this is a more interesting topic to the general public, so if the data set is rich for airlines I may not analyze private flight data.

----

# A5 Final Project Plan Work In Progress

## Background Research

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

----

## Notes for Reuse

For these data sets, accidents which were caused by an illegal act such as __suicide, sabotage, or terrorism__ were NOT included in rate calculations. However, it is factored in to the overall accident and fatality numbers. For example, 9/11 2001 terrorism fatalies & accidents are included but do not affect the rate calculations for accidents per million miles flown or fatalies per million miles flown. Additionally, only those killed on board the planes in the 9/11 terrorist attack are included in the fataly numbers. Unless otherwise stated all fatalies are on board fatalies. Information on acts of __Suicide, Sabotage, or Terrorism on 14 CFR 121 Flights__ are available [elsewhere](https://catalog.data.gov/dataset/air-carrier-occurrences-involving-illegal-acts-sabotage-suicide-or-terrorism-1995-through-).   

Some data is incomplete for 2015 and some data is incomplete for 2014, so only data through 2013 will be utilized. This is because a complete, verified, factual data is released every 5 years or so by the FAA. The next big release of records will be mid 2020 with a data set mostly complete through 2019.

Some of these data sets had headers at the top of the CSV or used two rows for the column label. These headers were deleted and dual row column labels combined in to a single row prior to other preprocessing steps in the Jupyter notebook.