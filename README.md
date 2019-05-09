# MapReduce

These examples include solutions generated on actual datasets retreived from Uber and Youtube. Datasets are inlcuded in respective folders.

Note: This is  python based examples.

# Uber

Problem 1: We will find the days on which each basement has more trips.

# Youtube

Problem 1: What are the top 5 categories with maximum number of videos uploaded.

Problem 2: Find the top 10 rated videos on youtube.

# Execute Commands

Go to the home Hadoop folder on your machine and write the following command on your terminal to execute a job. 

cat uber/uber.txt | mapperfile.extension | sort -k1,1 | reducerfile.extension

Mapper output is sorted ascendingly before being fed to reducer as input.
