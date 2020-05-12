# PART V
## GOAL
Example of  mapReduce to merge two datasets in one

### Datasets
clean_forum.tsv

forum_users.tsv

### Informations datasets
Merge a dataset of forum and a dataset of user wwhich wrote on this forum thanks to the authorID.
### clean_forum:
Contains all informations posts (split by a tab):

"postID", "title", "tagnames", "authorID", "body", "node_type", "parent_id", "abs_parent_ID", "addet_at", "score" ....

### forum_users:
Contains all informations of the author (split by a tab):

"authorID", "reputation", "gold", "silver", "bronze"

### To execute:
 hadoop jar [your_path]/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input [hadoop_path_datasets]/* -output [hadoop_path_folder_output]

### Output final (split by a tab):
"postID", "title", "tagnames", "authorID", "body", "node_type", "parent_id", "abs_parent_ID", "addet_at", "score", "reputation", "gold", "silver", "bronze"


### find.py
Find an author ID or a postID and give the reputation of the author. Use output file
