## Useful command: dasgoclient --query=" file dataset=/ScoutingPFRun3/Run2024H-v1/HLTSCOUT | grep file.name, file.size, file.nevents

datasets_query="dataset dataset=/*ZeroBias9*/*2018*/RAW" 
second_query="summary dataset=\$item" 

dasgoclient -query="$datasets_query" > datasets.txt
while read item; do eval dasgoclient -query=\"$second_query\"; done <  datasets.txt

## To get only the number of events directly: ##

while read item; do
    echo -n "$item    "
    dasgoclient -query="$second_query dataset=$item" | jq -r '.[0].num_event'
done < datasets.txt
