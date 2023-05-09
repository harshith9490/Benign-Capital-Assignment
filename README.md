# Benign-Capital-Assignment

1. Study about super trend indicator, it’s a very popular indicator, which can be easily understood through Google search.
2. Get Raw Market Data from this api https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
3. Apply super trend indicator to generate on each 5 min candle. You can use super trend variable as follows
ATR PERIOD = 7
MULTIPLIER = 3


# Super Trend Indicator
It was created by olivier seban\n
It will show the trend following indicator based on ATR(Average True Range)\n
It combines thge Trend Detection and volatility\n
Used to detect the changes in Trend Detection\n
Basic Upper Band = (high+low)/2 + (multiplier * ATR)\n
Basic lower Band = (high+low)/2 - (multiplier * ATR)\n

final upper band = if(previous final upper band > previous close ) \n
                      Then min(Basic upper Band , Previous Final Upper Band)
                   else
                       Basic Upper Band
                       

final lower band = if(previous final lower band < previous close ) 
                      Then max(Basic lower Band , Previous Final lower Band)
                   else
                       Basic lower Band
Super Trend = if(Previous super trend == Previous Final Upper Band AND Current Close <= Current Final Upper Band) OR
                 (Previous Super Trend == Previous Final Lower Band AND Current Close >= Current Fina Lower Band)
                Then
                   Previous Final Upper/Lower Band
              else
                    Current Super Trend
                    
