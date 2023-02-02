## hltGetConfig ... > hlt.py

from hlt import process
for stream in process.streams.parameters_():
    if "Parking" in stream or "Physics" in stream or "Scouting" in stream:
        print()
        for dataset in getattr(process.streams,stream).value():
            print( "%s (%s)"%(dataset,stream))
