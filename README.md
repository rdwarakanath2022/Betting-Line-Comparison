Welcome to Rishabh Dwarakanath's Sports Betting Line Comparison Machine

Why did I make this?
I wanted to see if I could replicate the services that large sports betting companies provide. By making my own,
it gives me the freedom to customize it as I see fit. I can use this machine to create lines that I can then compare to official lines to
see if some bets are worth taking. 

How:
I used public NFL statistics to grab the data I thought was most relevant to creating a line as similar to offical lines as possible. These statistics include QB rating, points per game, points per game allowed, etc. I formatted the data points into two csvs, an input and output. I then trained the model to match each line in the input csv to its corresponding line in the output csv. The model returns two values, the total point spread of the matchup, and the point spread projection. Ex (40, -3 -> Over/Under 40 total points, Home team favored to win by 3 points)

Expansion:
Currently working on expanding this model to create lines for the NBA, MLB, and NHL.