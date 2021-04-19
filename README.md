# Python DataFrame Processing Package - lcchendb Documentation
<b>Date:</b> Apr 18, 2021 <b>Version:</b> 1.0.0

## Environment Requirements

## Downloading
Download Package [here](https://github.com/lcchennn/sqldb_df/blob/688163ab22b904b5c77a41127486bf7b3388bcc2/lcchendb.py)
## Installing Package
Put the downloaded lcchendb.py file under 
..\Python\Pythonxx\Lib\site-packages
## Import Package
import lcchendb

## Examples
### lcchendb.readfromdf(path)
Reads csv file and return as df.
<br>*path:* File path, for example, 'https://raw.githubusercontent.com/lcchennn/sqldb_df/main/bread_noodle.csv'
<br><br>![image](https://user-images.githubusercontent.com/52438350/115191821-cbd5de80-a09e-11eb-8a0f-67a711b371ad.png)

### lcchendb.readfromdb(dbname, tablename)
Reads table from sqlite database as retun as df.
<br>*dbname:* SQLite database Name.
<br>*tablename:* Table name.
<br><br>![image](https://user-images.githubusercontent.com/52438350/115193726-66372180-a0a1-11eb-9fe8-a955e6c4abed.png)

### dftosqldb(df, tablename, dbname)
Reads table from csv file and writes to database.
<br>*df:* DataFrame name.
<br>*tablename:* Table name.
<br>*dbname:* SQLite database Name, for example, 'test.db'.
<br><br>![image](https://user-images.githubusercontent.com/52438350/115194521-6d126400-a0a2-11eb-983a-94705040aa74.png)
<br><br>![image](https://user-images.githubusercontent.com/52438350/115194795-cbd7dd80-a0a2-11eb-9b62-c542ff2bd622.png)

### lcchendb.dftosqlite(df, tablename, sqlfilename)
*df:* DataFrame name.
<br>*tablename:* Table name.
<br><br>*sqlfilename:* SQLite file Name, for example, 'test.sqlite'.

### lcchendb.common_column(df1, df2)
*df1:* Name of DataFrame 1.
<br>*df2:* Name of DataFrame 2.
<br><br>![image](https://user-images.githubusercontent.com/52438350/115195140-40ab1780-a0a3-11eb-8000-b759bc57bab3.png)


### lcchendb.npercnetile(df, input_pct)
*df:* DataFrame name.
<br>*input_pct:* Percentile.
<br><br>
![image](https://user-images.githubusercontent.com/52438350/115195202-515b8d80-a0a3-11eb-8714-4eddddabe06d.png)

## Tests
### 1. Get DataFrame Information
- Enter DataFrame name.
<br>![image](https://user-images.githubusercontent.com/52438350/115195382-8a93fd80-a0a3-11eb-8de6-96701777b5c0.png)
<br>- Return information.
<br>![image](https://user-images.githubusercontent.com/52438350/115195438-9bdd0a00-a0a3-11eb-9bd2-ff0d078c211c.png)

### 2. Get Percentile
- Enter DataFrame name and desired percentile.
<br>![image](https://user-images.githubusercontent.com/52438350/115195495-ae574380-a0a3-11eb-8fa7-e22f046d5695.png)
<br>- Return information.
<br>![image](https://user-images.githubusercontent.com/52438350/115195549-be6f2300-a0a3-11eb-912e-24b5332d1719.png)

### 3. Return Common DataFrame Columns
- Enter DataFrame names.
<br>![image](https://user-images.githubusercontent.com/52438350/115195595-cb8c1200-a0a3-11eb-8006-4b05075df9c7.png)
<br>- Return information.
<br>![image](https://user-images.githubusercontent.com/52438350/115195663-df377880-a0a3-11eb-9150-0af68c82418b.png)


