import pandas as pd
import glob

df = pd.read_excel('./FWF-Width-File.xlsx')



for file in sorted(glob('./SANITATION_TXT/*.TXT')): 
    col = df[df['Sheet'] == file.split('.')[0]]['Column Name'].tolist() 
    lenlist = df[df['Sheet'] == file.split('.')[0]]['Len'].tolist() 
    df_main = pd.read_fwf(file, widths=lenlist, header=None) 
    df_main.columns = col 
    df_main.to_excel(f'./SANITATION_XLSX/{file.split(".")[0]}' + '.xlsx') 

