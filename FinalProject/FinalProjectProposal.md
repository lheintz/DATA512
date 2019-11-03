# <center> Final Project Proposal </center>
<center> DATA 512 </center>
<center> Human Centered Data Science </center>
<center> Lauren Heintz  </center>
<center> 11/7/2019 </center>
 
 ----

## Motivation
While I am studying part time to become a data scientist, my full-time job is at The Boeing Company. There has recently been a lot of news and media on Boeing surrounding the 737Max crashes

----

## Data

| File Name |    Table Name    | Years | Data Source |
| ------ | ------------ | ------- | ----|
| accidentsAccidentRates_scheduledPass.csv | Accidents and Accident Rates by NTSB Classification, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121 | 1983 - 2014| https://catalog.data.gov/dataset/accidents-and-accident-rates-by-ntsb-classification-1995-through-2014-for-u-s-air-carriers |
| accidentsFatalitiesRates_airlines.csv | Accidents, Fatalities, and Rates, 1995 through 2014, for U.S. Air Carriers Operating Under 14 CFR 121, Scheduled and Nonscheduled Service (Airlines) | 1983 - 2014| https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-for-u-s-air-carriers-operating-under-14-c-dae36|
| accidentsFatalitiesRates_genAv.csv | Accidents, Fatalities, and Rates, 1995 through 2014, U.S. General Aviation | 1975 - 2014 | https://catalog.data.gov/dataset/accidents-fatalities-and-rates-1995-through-2014-u-s-general-aviation |
| faaAccidentIncidentDataSystem.csv | FAA Accident and Incident Data System (AIDS) | 1978 - 2015 | https://www.asias.faa.gov/apex/f?p=100:11:::NO::: |

## License 
> All data above information is federal government data, and therefore fits under the following free and open license: "U.S. Federal data available through [Data.gov](https://www.data.gov/privacy-policy#license) is offered free and without restriction. Data and content created by government employees within the scope of their employment are not subject to domestic copyright protection under 17 U.S.C. § 105." 

----

## Terms

| Term   | Definition |
| ----- | --- |
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

## Unknowns & Dependencies


----

## Notes for Reuse

For this analysis, only accidents for which were NOT an illegal act such as __suicide, sabotage, or terrorism__ were included. For example, 9/11 2001 terrorism fatalies & accidents are not included. Information on acts of __Suicide, Sabotage, or Terrorism on 14 CFR 121 Flights__ are available [elsewhere](https://catalog.data.gov/dataset/air-carrier-occurrences-involving-illegal-acts-sabotage-suicide-or-terrorism-1995-through-).   

Data is incomplete for 2015, so only data through 2014 will be utilized. This is because a complete, verified, factual data is released every 5 years by the FAA. The next big release of records will be mid 2020 with a data set only complete through 2019.