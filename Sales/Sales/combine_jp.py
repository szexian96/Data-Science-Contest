import os, glob
import pandas as pd
path = "/Users/szexian/Desktop/Data Science Contest/1-9/Sales/"
os.chdir(path)

extension = ('csv')
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,encoding="utf-8") for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')