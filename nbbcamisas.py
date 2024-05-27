from nbb_api import nbb
import pandas as pd
import matplotlib.pyplot as plt

temporadas = ['2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16',
            '2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23', '2023-24']

for temporada in temporadas:
    df = nbb.get_stats(season= temporada, fase='regular', tipo='sum', quem='athletes', categ='cestinhas' )
    df_agrupado = df.groupby('Camisa')['Pts'].sum().reset_index()
    df_agrupado_ordenado = df_agrupado.sort_values(by='Pts', ascending=False)
    ###print#(df_agrupado_ordenado.head())#

plt.barh(df_agrupado_ordenado, df_agrupado)
plt.show()
