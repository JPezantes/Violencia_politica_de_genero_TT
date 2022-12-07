"""
@author: Jose Pezantes

"""
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(@esthercuestasan OR @VickyDesintonio OR @anaraffo1 OR @SofiaEspinRC OR @marcelaholguin OR @RosaBelnMayorg1 OR @RaisaCorral OR @Alexandra_Arce OR @pierinaescorrea OR @Fernanda_Mashi OR @KatiuskaMEc OR @JessicaPk18 OR @Isabel_EJ OR @sofisanchezu OR @Wilmandrade OR @ConsueloVegaMS OR @luciaplacencia_ OR @yesguamani OR @zolandapluasec OR @dallyanapass OR @elinanarvaez25 OR @BrianaVillao OR @RinaCampainB OR @MCAquinoM OR @MJPlazaEc OR @BlankiSacancela) lang:es until:2022-10-17 since:2021-02-07"
tweets = []
limit = 20000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Text'])
print(df)

# to save to csv 
df.to_csv('tweets.csv') 