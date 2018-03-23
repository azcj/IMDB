# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:18:11 2017

@author: Nord
"""

#Aryana Collins Jackson
#R00169199
#Assignment 2

import numpy as np
import pandas as pd
import seaborn as sns
#import matplotlib.pyplot as plt

#load the csv into a dataframe and get rid of NAN values
df = pd.read_csv('movie_metadata.csv')
df=df.replace('?', np.nan)
df=df.dropna()
#print(df)

#part 1
def choice1(): 
    
    #create variable to keep going
    keepgoing = "y"

    while keepgoing=="y":  
        
        #ask the user to select direcctors or actors
        choice=int(input("Please select one: \n 1. Top directors \n 2. Top actors "))
        
        #if directors...
        if choice ==1:
            
            #ask the user to select the number of directors
            number=int(input("Please enter the number of directors you would like to look at: "))
            
            #make sure it's a valid number
            if number<1:
                print("Please enter a valid number.")
            elif number>len(df):
                print("This number exceeds the amount of rows in the data.")  
            
            #group the directors into a dictionary
            else:
                dirdf=df[['director_name' , 'gross']]
                directors=np.unique(dirdf['director_name'])
                dictionary={}
                
                #get the gross for each director and add it to the dictionary
                for director in directors:
                    newdffiltereddirector=dirdf[dirdf['director_name']==director]
                    totalgross=(np.sum(newdffiltereddirector['gross'])/1000000)
                    dictionary[director]=totalgross
                    
                #convert dictionary to pd series
                dic=pd.Series(dictionary) 
                dictplot=dic.sort_values(ascending=False).head(number)
                
                dictplot = dictplot.plot(x="director_name", y="gross",kind="barh")
                dictplot.set_xlabel("Gross Earnings (in billions)")
                dictplot.set_title("Top Gross Earnings")
        
        #if actors...
        elif choice==2:

            #ask the user to select a number of actors
            number = int(input("Please enter the number of actors you would like to look at: "))
            
            #make sure it's a valid number
            if number<1:
                print("Please enter a valid number.")
            
            elif number>len(df):
                print("This number exceeds the amount of rows in the data.")  
            
            #group the actors into a dictionary
            else:
                actdf=df[['actor_1_name' , 'gross']]
                allactors=np.unique(actdf['actor_1_name'])
                dictionary={}
                
                #get the gross for each actor and add it to the dictionary
                for actor in allactors:
                    newdffilteredactor=actdf[actdf['actor_1_name']==actor]
                    totalgross=(np.sum(newdffilteredactor['gross'])/1000000)
                    dictionary[actor]=totalgross
                    dic=pd.Series(dictionary) #convert dictionary to pd series
                    dictplot=dic.sort_values(ascending=False).head(number)
                    
                    dictplot = dictplot.plot(x="actor_1_name", y="gross",kind="barh")
                    dictplot.set_xlabel("Gross Earnings (in billions)")
                    dictplot.set_title("Top Gross Earnings")
        
        #ask the user to select another option if they have not selected 1 or 2
        else:
            keepgoing=input("That is an invalid number. Would you like to try again? y/n")

        #return the plot
        return dictplot

#part 2
def choice2():
    
    #strip out the weird character at the end of the title names
    df['movie_title'] = df['movie_title'].map(lambda x: x.rstrip('\xa0'))
    df['movie_title'] = df['movie_title'].map(lambda x: x.strip())
    
    keepgoing = "y"
    
    while keepgoing == "y":
        
        #ask user to enter first title
        input1 = input("Please enter the first film to compare: ")
        
        #make sure it matches
        if df["movie_title"].str.match(input1).any():
            keepgoing = "n"
        
        else:
            print("That is not a valid title.")
    
    keepgoing = "y"
    
    while keepgoing == "y":
        
        #ask user to enter second title
        input2 = input("Please enter the second film to compare: ")
        
        #make sure it matches
        if df["movie_title"].str.match(input2).any():
            keepgoing = "n"
            
        else:
            print("That is not a valid title.")
    
    keepgoing = "y"
    
    while keepgoing == "y":
        
        #ask user to select which option they want to compare
        choice = int(input("Please choose from the following options: \n 1. IMDB Scores \n 2. Gross Earnings \n 3. Facebook Likes "))
        
        #make sure it's a valid entry
        if choice == 1 or choice == 2 or choice == 3:
            keepgoing = "n"
            
        else:
            print("That is an invalid entry.")

    if choice == 1:
        
        #drop movies if they have no IMDB score
        df["imdb_score"] = df["imdb_score"].dropna()
        
        #match up the input with the data for that movie         
        if df["movie_title"].str.match(input1).any() and df["movie_title"].str.match(input1).any():
            
            #create the bar graph
            result = df[(df.movie_title == input1) | (df.movie_title == input2)]
            result = result.loc[:,["movie_title","imdb_score"]]
            result = result.plot(kind = 'bar', x = "movie_title")
            
            #label the bar graph
            result.set_xlabel("Title")
            result.set_ylabel("IMDB Score")
            result.set_title("IMDB Score Comparison")
            result.legend(["IMDB Score"])
            
            #print the graph
            result.plot(x="movie_title", y="imdb_score",kind="barh")
        
        else: 
            print("Sorry, there is no IMDB score comparison available.")
            
    if choice == 2:
        #drop movies if they have no IMDB score
        df["gross"] = df["gross"].dropna()
        
        #match up the input with the data for that movie        
        if df["movie_title"].str.match(input1).any() and df["movie_title"].str.match(input1).any():
            
            #create the bar graph
            result = df[(df.movie_title == input1) | (df.movie_title == input2)]
            result = result.loc[:,["movie_title","gross"]]
            result = result.plot(kind = 'bar', x = "movie_title")
            
            #label the bar graph
            result.set_xlabel("Title")
            result.set_ylabel("Gross Earnings")
            result.set_title("Gross Earnings Comparison")
            result.legend(["Gross Earnings"])
            
            #print the graph
            result.plot(x="movie_title", y="gross",kind="barh")
        
        else: 
            print("Sorry, there is no gross earnings comparison available.")
            
    if choice == 3:
        #drop movies if they have no IMDB score
        df["cast_total_facebook_likes"] = df["cast_total_facebook_likes"].dropna()
        
        #match up the input with the data for that movie
        if df["movie_title"].str.match(input1).any() and df["movie_title"].str.match(input1).any():
            
            #create the bar graph
            result = df[(df.movie_title == input1) | (df.movie_title == input2)]
            result = result.loc[:,["movie_title","cast_total_facebook_likes"]]
            result = result.plot(kind = 'bar', x = "movie_title")
            
            #label the bar graph
            result.set_xlabel("Title")
            result.set_ylabel("Total Facebook Likes")
            result.set_title("Facebook Likes Comparison")
            result.legend(["Facebook Likes"])
            
            #print the graph
            result.plot(x="movie_title", y="cast_total_facebook_likes",kind="barh")
        
        else: 
            print("Sorry, there is no Facebook likes comparison available.")

#part 3
def choice3():
    
    #concatinate gross earnings and title
    dfgrossyear=pd.concat([df.gross, df.title_year], axis=1)
    
    #sort the dataframe by year
    dfgrossyear=dfgrossyear.sort_values('title_year', ascending=False)

    #ask the user to select a start and end year
    start=int(input("Please enter a start year: ")) 
    end=int(input("Please enter an end year: ")) 

    #slice just the bit bewtween the years
    dfgrossyear2=dfgrossyear.loc[(dfgrossyear.title_year>=start)& (dfgrossyear.title_year<=end)]

    #group by year
    groupyear=dfgrossyear2.groupby('title_year')

    #make three lines
    dfmin=groupyear.min()
    dfmax=groupyear.max()
    dfmean=groupyear.mean()

    #print the plot
    result=pd.concat([dfmin, dfmax,dfmean], axis=1)
    result.columns=['min', 'max', 'mean']
    print(result)
    result = result.plot()
    result.set_xlabel("Year")
    result.set_ylabel("Gross (in billions)")
    result.set_title("Distribution of Gross Earnings")
    return result


def choice4():

    #split into strings
    df['genres'].str.split('|') 
    print("Action \n Adventure \n Animation \n) Biography \n Comedy \n Crime \n Documentary \n Drama \n Family \n Fantasy \n Film-Noir \n History \n Horror \n Music \n Musical \n Mystery \n Romance \n Sci-Fi \n Sport \n Thriller \n War \n Western")
    
    #ask user to input a genre
    inputgenre=input("Please select a genre: ")

    #make sure it is included in the list
    result = df['genres'].str.contains(inputgenre) 
    
    #print the series
    print(result) 
    test=(df[result])
    print("The mean is: ", round(test['imdb_score'].mean(),4))


def choice5():
    
    #print out each plot
    #the ones commented out don't provide any valuable information
    grid = sns.lmplot(x='imdb_score', y='gross', data=df) 
    grid.set(xlabel='IMDB Scores', ylabel='Gross Earnings')
    
    grid2 = sns.lmplot(x='imdb_score', y='num_critic_for_reviews', data=df)
    grid2.set(xlabel='IMDB Scores', ylabel='Number of Critic Reviews')
    
    grid3 = sns.lmplot(x='imdb_score', y='duration', data=df)
    grid3.set(xlabel='IMDB Scores', ylabel='Film Duration')
    
    #grid4 = sns.lmplot(x='imdb_score', y='director_facebook_likes', data=df)
    #grid4.set(xlabel='IMDB Scores', ylabel='Director Facebook Likes')
    
    #grid5 = sns.lmplot(x='imdb_score', y='actor_3_facebook_likes', data=df)
    #grid5.set(xlabel='IMDB Scores', ylabel='Actor 3 Facebook Likes')
    
    #grid6 = sns.lmplot(x='imdb_score', y='actor_1_facebook_likes', data=df)
    #grid6.set(xlabel='IMDB Scores', ylabel='Actor 1 Facebook Likes')
    
    grid7 = sns.lmplot(x='imdb_score', y='num_voted_users', data=df)
    grid7.set(xlabel='IMDB Scores', ylabel='Number of Users Who Voted')
    
    #grid8 = sns.lmplot(x='imdb_score', y='cast_total_facebook_likes', data=df)
    #grid8.set(xlabel='IMDB Scores', ylabel='Total Cast Facebook Likes')
    
    #grid9 = sns.lmplot(x='imdb_score', y='facenumber_in_poster', data=df)
    #grid9.set(xlabel='IMDB Scores', ylabel='Number of Faces in the Poster')
    
    grid10 = sns.lmplot(x='imdb_score', y='num_user_for_reviews', data=df)
    grid10.set(xlabel='IMDB Scores', ylabel='Number of User Reviews')
    
    #grid11 = sns.lmplot(x='imdb_score', y='budget', data=df)
    #grid11.set(xlabel='IMDB Scores', ylabel='Budget')
    
    #grid12 = sns.lmplot(x='imdb_score', y='actor_2_facebook_likes', data=df)
    #grid12.set(xlabel='IMDB Scores', ylabel='Actor 2 Facebook Likes')

def main():
 
    #set variable choice to input value
    choice=int(input("Please select: \n 1. Most successful directors and actors \n 2. Film comparison \n 3. Distributed gross earnings \n 4. Mean scores \n 5. IMDB score predicionts \n 6. Exit "))
    
    #run through each function
    if choice == 1:
        choice1() 
        
    elif choice == 2:
        choice2()
        
    elif choice == 3: 
        choice3() 
        
    elif choice == 4:
        choice4()
        
    elif choice == 5: 
        choice5()
        
    elif choice==6:
        print("You have chosen to exit, goodbye!")
        
    else:
        print("That is an invalid number.")

main()
     

    