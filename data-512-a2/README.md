# Bias in Data

Name: Lauren Heintz

Date: 10/17/2019

## Goal
The goal of this project is to identify sources of bias in country politician pages on wikipedia. In looking at all of the pages on political figures on wikipedia, we can start to dig in to countries that may be underrepresented or over represented. The quality of these articles will also be analyzed, using an existing prediction model called ORES which generates a quality score for wikipedia pages. In the end, I hope to summarize my findings on possible sources of bias in this data set as well as outline my methodology for analysis. Details can be found in the Jupyter notebook in this repo.

## Data sources used

To create these tables, we will draw from three data sources:
1. [Politician wikipedia page by country data set](https://figshare.com/articles/Untitled_Item/5513449).   
2. [World population dataset](https://www.prb.org/international/indicator/population/table/).   
3. [ORES REST API Endpoint](https://ores.wikimedia.org/v3/#!/scoring/get_v3_scores_context_revid_model)

## Data Definition
Politician Page Data Set
> * page name : The name of the wikipedia name, which is also the name of the politician in this case 
> * country : the country from which the politician is from  
> * rev id : the revision ID number - which is a unique key to a version of the page at a given point in time

World Population Data Set
> * population : The population of the given country in millions
> * country : the country 
> * region : the world was divided in to geographic regions and each country is assigned one of these regions

ORES REST API Data Set
> * rev id : the revision ID number - which is a unique key to a version of the page at a given point in time
> * prediction : the predicted value of the model rating the quality of the article. Possible prediction are as follows, in order of highest quality to worst quality article:
> 1. FA - Featured article
> 2. GA - Good article
> 3. B - B-class article
> 4. C - C-class article
> 5. Start - Start-class article
> 6. Stub - Stub-class article


## Resources used
The tools used on this project were Anacoda 4.6.14, Python 3.6, VSCode 1.30.1, Jupyter Notebook 5.7.4, and linux terminal. Operating system was MacOSX Mojave 10.14.6   
>Documentation for Python can be found here: https://docs.python.org/3.6/    
Documentation for Jupyter Notebook can be found here: http://jupyter-notebook.readthedocs.io/en/latest/   
Documentation for Anaconda can be found here: https://www.anaconda.com/distribution/  
Documentation for VSCode can be found here: https://code.visualstudio.com/   

The following Python packages were used and their documentation can be found at the accompanying links:
>pandas: https://pandas.pydata.org/  
numpy: https://numpy.org/  
requests: https://pypi.org/project/requests/2.7.0/  
json: https://docs.python.org/3/library/json.html   

## Files Created
This notebook creates 11 CSV files of data extracted and compiled as part of this analysis. Specific details as to the contents of these CSVs and the process to create them is in the Jupyter Notebook in this repo. For all intents and purposes the final cleaned data set is `results` > `wp_wpds_politicians_by_country.csv`, which contains the population data, page data, and prediction data all joined in one table.

data_clean  
>    GeographyRollUp.csv  
    ores_no_score.csv  
    pred_scores.csv  
    wp_wpds_countries_no_match.csv  
    wp_wpds_politicians_by_country.csv  

results  
>    table1.csv  
    table2.csv  
    table3.csv  
    table4.csv  
    table5.csv  
    table6.csv  
    wp_wpds_politicians_by_country.csv  

In the process of parsing the json files from the ORES API, a couple of additional files were generated and overwritten in the data_raw folder as a script ran to process the download of information. In this process, not all revision IDs were found to have predictions returned from the ORES model. Revision IDs for which no predictions were found are in the  `data_clean` > `ores_no_score.csv`. 

## Visualizations Created

Several tables are displayed in the jupyter notebook, the data from these tables are saved as aa csv in the results folder.

## License

This assignment code is released under the MIT license in this repo.

The politician page count data is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

The ORES Rest API is licensed by CC-SA.

## Notes for Reuse / Special Considerations

Some notes in regards to the analysis work done. For the analysis of the relative number of good quality articles versus total articles, countries with zero good quality articles were discarded. This is because items with zero good articles sometimes only had a handful of articles written at all. We are more interested in countries with a huge disparity between good articles and total articles, because this could indicate something about the bias in the overall sample set for this country. For this reason, items with zero good articles were discarded in favor of items with at least 1 good article so that a proper proportion could be calculated. 