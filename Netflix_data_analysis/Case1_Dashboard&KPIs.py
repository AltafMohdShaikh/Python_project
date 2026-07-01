# 🎬 Case Study 1: Netflix Content Overview
# Business Problem
# Netflix management wants a high-level overview of the content library.

# Tasks
# Total Movies
# Total TV Shows
# Total Titles
# Number of Countries
# Oldest Release Year
# Latest Release Year
# Movies vs TV Shows
# Content Added Per Year

# Deliverable
# Create a dashboard with KPIs and visualizations.


import pandas as pd
df = pd.read_csv('netflix_titles.csv')
df.head()


# Remove leading/trailing spaces
df['date_added'] = df['date_added'].str.strip()

# Convert to datetime
df['date_added'] = pd.to_datetime(df['date_added'])
df['release_year'] = pd.to_datetime(df['release_year'])


df.info()


# Total Movies
totalmovies = df['show_id'].nunique()

# Total TV Shows
totalTvShows = df[df['type'] == 'TV Show']['show_id'].nunique()

# Total title
totaltitle = df['title'].nunique()

# Number of Countries
totalCountries = (
    df['country']
      .dropna()
      .str.split(',')
      .explode()
      .str.strip()
      .nunique()
)

# Oldest Release Year
oldestrelease = df['release_year'].min()

# Latest Release Year
latestrelease = df['release_year'].max()

# Movies vs TV Shows
moviesVsTvshows = df['type'].value_counts()

# Content Added Per Year
# df['year_added'] = df['date_added'].dt.year
content_added_per_year = df.groupby(df['date_added'].dt.year).size()


# dashboard and KPIs

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(16,10))


# Movies vs TV Shows
moviesVsTvshows.plot(
    kind='bar',
    ax=ax[0,0],
    color=['red', 'blue']
)
ax[0,0].set_title("Movies vs TV Shows")
ax[0,0].set_xlabel("")
ax[0,0].set_ylabel("Count")


# Content Added Per Year
content_added_per_year.plot(
    kind='line',
    marker='o',
    ax=ax[0,1]
)

ax[0,1].set_title("Content Added Per Year")
ax[0,1].set_xlabel("Year")
ax[0,1].set_ylabel("Titles Added")


# KPI Cards
ax[1,0].axis("off")

kpis = f"""
Total Titles      : {totaltitle}
Movies            : {totalmovies}
TV Shows          : {totalTvShows}
Countries         : {totalCountries}
Oldest Release    : {oldestrelease}
Latest Release    : {latestrelease}
"""

ax[1,0].text(
    0.3,
    0.8,
    kpis,
    fontsize=14,
    va='top',
    family='monospace'
)

ax[1,0].set_title("Netflix KPIs")

# Empty subplot
ax[1,1].axis("off")

plt.tight_layout()
plt.show()
plt.show()

