# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:07:02 2018

@author: jonatha.costa
"""

import requests 
import pandas as pd


def election_data(datai, dataf,save = True,unidade_federativa_p = 6, ano_p = 2018,turno_p = "T", cargos_id_p = 3, order_column_p = 'ano', tipo_id_p = 'T'):

    url_base = "https://pesquisas.poder360.com.br/web/consulta/fetch?"
    unidade_federativa = unidade_federativa_p
    ano = ano_p
    data_pesquisa_de = datai
    data_pesquisa_ate = dataf
    turno = turno_p
    tipo_id = tipo_id_p
    cargos_id = cargos_id_p
    order_column = order_column_p
    url_fragment =  "unidades_federativas_id=" +  unidade_federativa  + "&cargos_id=" + cargos_id +"&ano="+ ano +"&data_pesquisa_de="+ data_pesquisa_de + "&data_pesquisa_ate="+  data_pesquisa_ate + "&turno=" + turno +"&tipo_id="+ tipo_id +"&order_column="+ order_column + "&order_type=asc"
    url_request = url_base + url_fragment
    req = requests.get(url = url_request)
    data = req.content
    df = pd.read_json(data)
    if(save):    
        df.to_csv("df_eleicoes_2018.csv",sep = ";", encoding = "utf-8")
    else:
        return(df)
