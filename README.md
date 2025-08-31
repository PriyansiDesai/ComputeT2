# UFC Fighters Data Analysis

# What I did
Explored and cleaned the UFC fighters dataset. Checked out their height, weight, reach, wins, losses, draws and stance. Filled missing stuff, removed duplicates, and looked for outliers.

# Dataset
Contains info about fighters:
- name, nickname
- wins, losses, draws
- height, weight, reach
- stance, date of birth
- fighting stats like strikes, takedowns, submissions

# Cleaning
- Missing numbers (height, weight, reach) : used median
- Missing stance : used most common one
- Missing nicknames : added 'No nickname'
- Removed duplicate rows
- date_of_birth still has some missing,didnt change

# What I saw / Plots
I made histograms and boxplots to check the distributions and spot outliers in the numbers, countplots to see how stances are spread, scatter plots to see trends like height and weight versus wins, and a correlation heatmap to figure out what features relate to wins. From this, I noticed that taller fighters with longer reach tend to win more, Orthodox is the most common stance while Southpaw fighters seem to win a bit more on average, and there are some crazy outliers in wins and losses, but those are just real top fighters.

# What I can do next
- Look at trends by weight class
- Try to predict fight results
