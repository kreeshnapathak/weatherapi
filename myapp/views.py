from django.shortcuts import render
import json
from urllib.request import urlopen
import requests



# Create your views here.
def home(request):
    res=requests.get("https://ipinfo.io?token=a8077b42f5d3fd")
    # print(res.text)
    if request.method=="POST":
        city=request.POST["ct"]
        try:
            with urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid=d1bb0beb1769d3252b9ae09d8b16368b') as response:
                source=response.read()
           
            data=json.loads(source)
        

            alldata={
                "country_code": str(data['sys']['country']),
                "coordinate": str(data['coord']['lon'])+','+str(data['coord']['lat']),
                "temperature": str(data['main']['temp']),
                "pressure": str(data['main']['pressure']),
                "humidity": str(data['main']['humidity']),
                "description": str(data['weather'][0]['description']),
                "icon": data['weather'][0]['icon'],
                "name":data['name']
            }
                
            # print(f"{data['coord']['lon']} {data['coord']['lat']}")
            # a=(data['weather'][0]['description'])
            # print(a)
            # print(alldata)
            return render(request,'myapp/home.html',alldata)
        except:
            return render(request,'myapp/home.html')

    else:
        return render(request,'myapp/home.html')

    
    