## Useful command: dasgoclient --query=" file dataset=/ScoutingPFRun3/Run2024H-v1/HLTSCOUT | grep file.name, file.size, file.nevents

datasets_query="dataset dataset=/*ZeroBias9*/*2018*/RAW" 
second_query="summary dataset=\$item" 

dasgoclient -query="$datasets_query" > datasets.txt
while read item; do eval dasgoclient -query=\"$second_query\"; done <  datasets.txt
