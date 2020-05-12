# PART V
## GOAL
Example of  mapReduce to merge two datasets in one

### Datasets
clean_forum.tsv

forum_users.tsv

Merge these 2 datasets with authorID.

### To execute:
 hadoop jar [your_path]/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input [hadoop_path_datasets]/* -output [hadoop_path_folder_output]

### Output final (split by a tab):
[postID] \t [title] \t [tagnames] \t [authorID] \t [body] \t [node_type] \t [parent_id] \t [abs_parent_ID] \t [addet_at] \t [score] \t [reputation] \t [gold] \t [silver] \t [bronze]


### find.py
Find an author ID or a postID and give the reputation of the author. Use output file
