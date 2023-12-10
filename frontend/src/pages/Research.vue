<script setup>
  import H1Text from '@/components/H1Text.vue';
  import H2Text from '@/components/H2Text.vue';
  import PText from '@/components/PText.vue';
  import CodeText from '@/components/CodeText.vue';
  import PlotImg from '@/components/PlotImg.vue';
  import TableDescription from '@/components/TableDescription.vue';
  import Boxplots from '@/components/Boxplots.vue';
  import Statistic from '@/components/Statistic.vue';
  import GlobalListener from '@/components/GlobalListener.vue';
  import Header from '@/components/Header.vue';
  import Footer from '@/components/Footer.vue';
  import Icefall from '@/components/Icefall.vue';
</script>

<template>
  <header>
    <Header/>
    <GlobalListener/>
  </header>

  <main>
    <Icefall/>
    <img id="logo" src="@/assets/bigfoot.svg"/>
    <p id="title-text">Searching for Bigfoot<br/>project 2012</p>
    <H1Text>Main goal of the project</H1Text>
    <PText>The main goal of this project is to understand the conditions under which the bigfoot is most likely to appear, to find out under what circumstances people have seen it or traces of its existence.</PText>
    <H1Text>Hypothesis</H1Text>
    <PText>My hypothesis is that the bigfoot is most often found in winter, at low temperatures, in the most northern or mountainous areas of America.</PText>
    <H1Text>Analyze data from the table</H1Text>
    <PText>I chose a dataframe of actual Bigfoot encounter reports collected by bfro.net for processing. The data is available in the form of a table, which contains the columns described below.</PText>
    <H2Text>Table description</H2Text>
    <TableDescription/>
    <H1Text>Preparing for analysis</H1Text>
    <PText>To begin with, it is necessary to import all libraries required in this project and read our dataframe with pandas.</PText>
    <CodeText height="285">
import pandas as pd<br/>
from pandas.api.types import is_numeric_dtype<br/>
from datetime import date<br/>
import seaborn as sns<br/>
import matplotlib.pyplot as plt<br/>
import matplotlib.patches as mpatches<br/>
import matplotlib.cm as mcm<br/>
import matplotlib.dates as mdates<br/>
import numpy as np<br/>
<br/>
df = pd.read_csv('data/bfro_reports_geocoded.csv')<br/>
    </CodeText>
    <PText>Then I want to prepare the data for working, as some formats or cells may cause inconveniences in further work.</PText>
    <H2Text>Create a convient dataframe for analyzing dates</H2Text>
    <CodeText height="630">
date_df = df[['date']].copy()<br/>
date_df.dropna(inplace=True)<br/>
date_df['Year'] = pd.to_datetime(date_df['date'],<br/>
&nbsp;format='%Y-%m-%d').dt.year<br/>
date_df['Month'] = pd.to_datetime(date_df['date'],<br/>
&nbsp;format='%Y-%m-%d').dt.month<br/>
date_df['Day'] = pd.to_datetime(date_df['date'],<br/>
&nbsp;format='%Y-%m-%d').dt.day<br/>
<br/>
this_year = date.today().year<br/>
date_df = date_df[date_df['Year']  this_year]<br/>
date_df = date_df[date_df['Year'] > 1957]<br/>
<br/>
month_dict = {<br/>
&nbsp;1: 'January',<br/>
&nbsp;2: 'February',<br/>
&nbsp;3: 'March',<br/>
&nbsp;4: 'April',<br/>
&nbsp;5: 'May',<br/>
&nbsp;6: 'June',<br/>
&nbsp;7: 'July',<br/>
&nbsp;8: 'August',<br/>
&nbsp;9: 'September',<br/>
&nbsp;10: 'October',<br/>
&nbsp;11: 'November',<br/>
&nbsp;12: 'December'<br/>
}<br/>
date_df['Month'] = date_df['Month'].map(month_dict)<br/>
    </CodeText>
    <H2Text>Changing degrees Fahringheit to Celsius</H2Text>
    <CodeText height="255">
def FtoC(df, col):<br/>
df[col] = (df[col] - 32) * 5/9<br/>
&nbsp;return df<br/>
<br/>
df = FtoC(df, 'temperature_high')<br/>
df = FtoC(df, 'temperature_mid')<br/>
df = FtoC(df, 'temperature_low')<br/>
    </CodeText>
    <PText>And the last step before we start depicting our data as charts is to set the styles that are common to them.</PText>
    <CodeText height="330">
font_prop = fm.FontProperties(fname='./FugazOne-Regular.ttf', size=12)<br/>
plt.rcParams['figure.dpi'] = 300<br/>
plt.rcParams['savefig.dpi'] = 300<br/>
text_color = "#4e5f92"<br/>
plt.rcParams['font.family'] = 'monospace'<br/>
plt.rcParams['font.monospace'] = 'Nimbus Sans'<br/>
plt.rcParams["font.weight"] = "bold"<br/>
plt.rcParams['text.color'] = text_color<br/>
plt.rcParams['axes.titlecolor'] = text_color<br/>
plt.rcParams['axes.labelcolor'] = text_color<br/>
plt.rcParams['axes.edgecolor'] = text_color<br/>
plt.rcParams['xtick.color'] = text_color<br/>
plt.rcParams['ytick.color'] = text_color<br/>
    </CodeText>
    <H1Text>Simple analysis</H1Text>
    <PText>First of all, let's try to look at the various numerical values we have, find mean, median and standart deviation for each parameter and illustrate them on the boxplot.</PText>
    <H2Text>Generate boxoplots</H2Text>
    <CodeText height="775">
def get_boxplot(df, col, title):<br/>
&nbsp;if(is_numeric_dtype(df[col])):<br/>
&nbsp;&nbsp;fig = plt.figure(figsize=(5, 5))<br/>
&nbsp;&nbsp;fig.set_facecolor('#e6edff')<br/>
&nbsp;&nbsp;plt.gca().set_facecolor('#e6edff')<br/>
&nbsp;&nbsp;cmap = mcm.get_cmap('viridis')<br/>
<br/>
&nbsp;&nbsp;colors = cmap(np.linspace(0.2, 1, 3))<br/>
<br/>
&nbsp;&nbsp;this_df = df[col]<br/>
&nbsp;&nbsp;this_df.dropna(inplace=True)<br/>
&nbsp;&nbsp;sns.boxplot(<br/>
&nbsp;&nbsp;&nbsp;y=this_df.to_numpy(),<br/>
&nbsp;&nbsp;&nbsp;showmeans=True,<br/>
&nbsp;&nbsp;&nbsp;width=0.4,<br/>
&nbsp;&nbsp;&nbsp;meanline=True,<br/>
&nbsp;&nbsp;&nbsp;meanprops={'color': '#7ecfcd', 'ls': '-', 'lw': 2},<br/>
&nbsp;&nbsp;&nbsp;medianprops={'color': '#2a3359', 'ls': '-', 'lw': 2},<br/>
&nbsp;&nbsp;&nbsp;palette=colors<br/>
&nbsp;&nbsp;)<br/>
<br/>
&nbsp;&nbsp;mean_patch = mpatches.Patch(color='#7ecfcd', label='Mean')<br/>
&nbsp;&nbsp;median_patch = mpatches.Patch(color='#2a3359', label='Median')<br/>
<br/>
&nbsp;&nbsp;plt.title(f"{title} Boxplot", fontproperties=font_prop)<br/>
&nbsp;&nbsp;plt.legend(<br/>
&nbsp;&nbsp;&nbsp;handles=[mean_patch, median_patch],<br/>
&nbsp;&nbsp;&nbsp;loc='lower right',<br/>
&nbsp;&nbsp;&nbsp;frameon=False<br/>
&nbsp;&nbsp;)<br/>
&nbsp;&nbsp;sns.despine()<br/>
&nbsp;<br/>
&nbsp;&nbsp;plt.show()<br/>
&nbsp;else:<br/>
&nbsp;&nbsp;return "Numeric col required"<br/>
    </CodeText>
    <Boxplots/>
    <Statistic/>
    <PText>Of interest, here we can notice that for bigfoot sighting humidity and dew point should be higher than the regional average (America - average humidity varies from 25 to 65%). Precipitation probability and intensity, moon phase, pressure, UV index, cloud coverage, visibility, wind bearing and speed and even temperature - do not have effect on sighting probability (they're regional averages).</PText>
    <PText>The next step is to analyze the dates of bigfoot sightings, for which we will use the prepared for analyze date dataframe.</PText>
    <H2Text>Get sightings by year</H2Text>
    <CodeText height="575">
ax = date_df['Year'].value_counts().sort_index()<br/>
cmap = mcm.get_cmap('Blues')<br/>
colors = cmap(np.linspace(0.2, 1, len(ax.values) + 80))[::-1]<br/>
<br/>
fig = plt.figure(figsize=(12, 6))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
sns.barplot(<br/>
&nbsp;x = ax.index,<br/>
&nbsp;y = ax.values,<br/>
&nbsp;palette=colors,<br/>
&nbsp;hue=ax.index,<br/>
&nbsp;legend=False<br/>
)<br/>
plt.xlabel('Year', fontproperties=font_prop)<br/>
plt.ylabel('Incident Count', fontproperties=font_prop)<br/>
plt.title('Bigfoot Sightings by year', fontproperties=font_prop)<br/>
plt.xticks(<br/>
&nbsp;ticks=np.arange(0, len(ax.index), 5),<br/>
&nbsp;labels=ax.index[::5]<br/>
)<br/>
<br/>
sns.despine()<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="years.png"/>
    <PText>Here we can notice the wavelike movement of the chart (a kind of eliot waves). Thus, we only can conclude that the popularity of bigfoot and the number of reports of sightings are likely to grow soon.</PText>
    <H2Text>Get sightings by month</H2Text>
    <CodeText height="455">
month_counts = date_df['Month'].value_counts()<br/>
colors = mcm.get_cmap('viridis', 40)<br/>
<br/>
fig = plt.figure(figsize=(8, 6))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
plt.pie(<br/>
&nbsp;month_counts,<br/>
&nbsp;labels = month_counts.index,<br/>
&nbsp;colors=colors(range(12)),<br/>
&nbsp;wedgeprops={<br/>
&nbsp;&nbsp;'edgecolor': '#e6edff',<br/>
&nbsp;&nbsp;'width': 0.3,<br/>
&nbsp;&nbsp;'linewidth': 3<br/>
&nbsp;}<br/>
)<br/>
plt.title('Bigfoot Sightings by month', fontproperties=font_prop)<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="months.png" width="750px"/>
    <PText>Here we can notice that the number of sightings is higher in summer and autumn, which is logical, because in winter and spring it is cold and there is a lot of snow in the forests, which makes it difficult to move around.</PText>
    <PText>As a final step in this section, I would like to analyze the distribution of sightings by class and state.</PText>
    <H2Text>Get sightings by class and state</H2Text>
    <CodeText height="595">
params = {<br/>
&nbsp;"state": {<br/>
&nbsp;&nbsp;"name": "State",<br/>
&nbsp;&nbsp;"colors": 70<br/>
&nbsp;},<br/>
&nbsp;"classification": {<br/>
&nbsp;&nbsp;"name": "Class",<br/>
&nbsp;&nbsp;"colors": 4<br/>
&nbsp;}<br/>
}<br/>
<br/>
for param in ["state", "classification"]:<br/>
&nbsp;cmap = mcm.get_cmap('Blues')<br/>
&nbsp;colors = cmap(np.linspace(0.2, 1, params[param]['colors']))[::-1]<br/>
&nbsp;<br/>
&nbsp;fig = plt.figure(figsize=(12, 6))<br/>
&nbsp;fig.set_facecolor('#e6edff')<br/>
&nbsp;plt.gca().set_facecolor('#e6edff')<br/>
<br/>
&nbsp;sns.histplot(df, x=param, hue=param, palette=colors, legend=False, linewidth=0)<br/>
&nbsp;plt.xticks(rotation=90) <br/>
&nbsp;plt.xlabel(params[param]["name"], fontproperties=font_prop)<br/>
&nbsp;plt.ylabel('Incident Count', fontproperties=font_prop)<br/>
&nbsp;plt.title('Bigfoot Sightings by ' + params[param]["name"], fontproperties=font_prop)<br/>
&nbsp;sns.despine()<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="classes.png"/>
    <PlotImg name="states.png"/>
    <PText>Here we can see quite logical conclusions that the bigfoot is most often noticed in the state of Washington (as it is in the northwest of the United States is supposedly its habitat zone).</PText>
    <PText>Regarding the classes we can notice very little presence of class C in the dataframe, as the description says that class C is mostly stored in the BFRO archives and only some exceptional cases are included here.</PText>
    <H1Text>Advanced analysis</H1Text>
    <PText>To start a deeper analysis we need to build a table that can be used to find the correlations between the parameters of our dataframe.</PText>
    <H2Text>Get correlations</H2Text>
    <CodeText height="270">
fig = plt.figure(figsize=(15, 7))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
corr = df.corr(numeric_only = True)<br/>
upper_triangle = np.triu(np.ones_like(corr, dtype=bool))<br/>
<br/>
sns.heatmap(corr,vmin = -1, vmax = 1, cmap = "Blues", annot = True, mask = upper_triangle)<br/>
plt.title("Correlation of all features and target", fontproperties=font_prop)<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="correlations.png"/>
    <PText>I could not find any important information here, as all values with high correlations are already logically connected (e.g. highest and lowest temperatures for the day).</PText>
    <PText>At this stage of the study, I was a little stuck, but still decided to analyze the relationship between the lowest and highest temperature and humidity. Humidity was chosen due to the fact that this indicator showed a difference with the average value in the analysis of boxplots.</PText>
    <H2Text>Get humidity by highest and lowest temperature</H2Text>
    <CodeText height="590">
fig = plt.figure(figsize=(12, 6))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
sns.scatterplot(<br/>
&nbsp;df,<br/>
&nbsp;x="temperature_high",<br/>
&nbsp;y="temperature_low",<br/>
&nbsp;hue="humidity",<br/>
&nbsp;palette="Blues",<br/>
&nbsp;linewidth=0,<br/>
)
plt.title("Highest and lowest temperature of sighting by humidity",<br/>
fontproperties=font_prop)<br/>
plt.xlabel("Highest temperature (C)", fontproperties=font_prop)<br/>
plt.ylabel("Lowest temperature (C)", fontproperties=font_prop)<br/>
sns.despine()<br/>
plt.legend(title="Humidity", loc='upper left', frameon=False)<br/>
<br/>
plt.axline(<br/>
(
&nbsp;df['temperature_high'].mean(),<br/>
&nbsp;df['temperature_low'].mean()),<br/>
&nbsp;slope=1,<br/>
&nbsp;color='#440154',<br/>
&nbsp;linestyle='--'<br/>
)<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="temp-hum.png"/>
    <PText>Here we can see that humidity correlates with temperature difference. Thus, with a decrease in the LT/HT ratio, the humidity during observation decreases significantly. But since the average humidity in the dataframe is higher than the average humidity in the region, bigfoot can be found with the greatest temperature difference.</PText>
    <PText>My last research related to temperature concerns classes and regions, or rather their longitude. The lighter points here will indicate the more northern regions</PText>
    <H2Text>Get sightings by temperature, class and longitude</H2Text>
    <CodeText height="470">
fig = plt.figure(figsize=(12, 6))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
sns.stripplot(<br/>
&nbsp;df,<br/>
&nbsp;x="classification",<br/>
&nbsp;y="temperature_mid",<br/>
&nbsp;palette="Blues",<br/>
&nbsp;hue="longitude",<br/>
&nbsp;size=3,<br/>
&nbsp;legend=False,<br/>
&nbsp;linewidth=0,<br/>
)<br/>
plt.title("Class distribution by temperature", fontproperties=font_prop)<br/>
plt.xlabel("Class", fontproperties=font_prop)<br/>
plt.ylabel("Temperature (C)", fontproperties=font_prop)<br/>
sns.despine()<br/>
<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="temp-class.png"/>
    <PText>We can see that Class A messages are much more logically grouped in terms of temperature and longitude ratio than Class B messages. This confirms the great reliability of the Class A reports.</PText>
    <PText>In the last graph, I would like to depict the distributions of sightings by state and season.</PText>
    <H2Text>Get sightings by state and season</H2Text>
    <CodeText height="480">
cmap = mcm.get_cmap('Blues')<br/>
colors = cmap(np.linspace(0.2, 1, 5))<br/>
fig = plt.figure(figsize=(12, 6))<br/>
fig.set_facecolor('#e6edff')<br/>
plt.gca().set_facecolor('#e6edff')<br/>
<br/>
sns.histplot(<br/>
&nbsp;df,
&nbsp;x="state",<br/>
&nbsp;hue="season",<br/>
&nbsp;palette=colors,<br/>
&nbsp;multiple="stack",<br/>
&nbsp;linewidth=0<br/>
)<br/>
<br/>
plt.xticks(rotation=90)<br/>
plt.xlabel('State', fontproperties=font_prop)<br/>
plt.ylabel('Incident Count', fontproperties=font_prop)<br/>
plt.title('Bigfoot Sightings by state', fontproperties=font_prop)<br/>
sns.despine()<br/>
plt.show()<br/>
    </CodeText>
    <PlotImg name="class-state.png"/>
    <PText>Here we can notice that even despite the distribution by state, the seasons remain the same for almost every state. Bigfoot is most often found in autumn or summer, regardless of the region.</PText>
    <H1Text>Conclusion</H1Text>
    <PText>The conclusion completely refutes the hypothesis. Bigfoot is most likely to be found in summer or autumn in the hilly area of Washington State on days with the greatest temperature difference and high humidity. At the same time, even these correlations are weak, from which it can be concluded that the messages about bigfoot are extremely random.</PText>
    <Footer/>
  </main>
</template>
    

<style scoped lang="scss">
  #logo {
    width: 15vw;
    display: block;
    margin: 0 auto 2rem;
    margin-top: 250px;
  }
  #title-text {
    margin: 0;
    font-family: 'Rubik Bubbles', serif;
    font-size: 5rem;
    color: #4e5f92;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 160px;
  }
  @media (max-width: 750px) {
    #logo {
      width: 50vw;
    }
    #title-text {
      font-size: 4rem;
    }
  }
</style>
