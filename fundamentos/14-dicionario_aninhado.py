seriesDict ={
    "GOT":{
         "title": "Game of Thrones",
    "releaseYear": 2011,
    "rating": 9.8,
    "genre": ["Fantasy", "Medieval"]
    },
    "Flash": {
        "title": "The Flash",
    "releaseYear": 2010,
    "rating": 8.5,
    "genre": ["Hero", "Action"]
    }
}


print(seriesDict)

print(seriesDict["Flash"]["genre"])

seriesDict["Flash"]["director"] = "Andrés Muschietti"
print(seriesDict["Flash"]["director"])

del seriesDict["Flash"]
print(seriesDict)