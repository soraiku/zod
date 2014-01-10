# -*- coding: utf-8 -*-
import datetime
import math
import random
import string

def my_view(request):
  return {'project':'newproject'}

def home_view( request ):
  img=("0.jpg","1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg","11.jpg")
  imgs=len(img)
  return {"imgs":imgs,"img": img}

def zodiac_view(request):
  #arrays
  img=("0.jpg","1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg","10.jpg","11.jpg")
  signe=("CAPRICORNIO","ACUARIO","PISCIS","ARIES","TAURO","GEMINIS","CANCER","LEON","VIRGO","LIBRA","ESCORPION","SAGITARIO")
  dates=(20,19,20,20,21,21,22,22,22,22,22,21)
  frase=("TE PASARA ALGO INESPERADO","TE RODEA LA BUENA SUERTE, APROVECHALA","CONOCERAS A UN PERSONA QUE SE CONVERTIRA MUY IMPORTANTE")
    
  
  #agafar la variable del formulari
  data = request.POST.get("data")
  if not data:
    return {}
    
    
  #variable que agafar l'any el mes i el dia
  year, month, day = map(int, data.split('/'))
  date1=datetime.date(year,month,day)
  
  #numero aleatori per escollir la frase aleatori
  num=random.randint(0,2)
  
  #variables necessàries per fer el calcul
  dia=date1.day
  mes=date1.month
  mes=mes-1
  
  if dia>dates[mes]:
    mes=mes+1
  if mes==12:
    mes=0
    
    
  return {"horoscop":signe[mes],"frase":frase[num],"imatges":img[mes]}
