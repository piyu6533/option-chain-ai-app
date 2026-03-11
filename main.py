from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import requests

URL="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

class Dashboard(BoxLayout):

```
def update(self,dt):

    headers={"User-Agent":"Mozilla/5.0"}

    s=requests.Session()
    s.get("https://www.nseindia.com",headers=headers)

    data=s.get(URL,headers=headers).json()

    spot=data["records"]["underlyingValue"]

    call_oi=0
    put_oi=0

    for row in data["records"]["data"]:

        if "CE" in row:
            call_oi+=row["CE"]["openInterest"]

        if "PE" in row:
            put_oi+=row["PE"]["openInterest"]

    pcr=round(put_oi/call_oi,2)

    signal="SIDEWAYS"

    if pcr>1.2:
        signal="BUY"

    elif pcr<0.8:
        signal="SELL"

    self.ids.spot.text="Spot: "+str(spot)
    self.ids.pcr.text="PCR: "+str(pcr)
    self.ids.signal.text="Signal: "+signal
```

class TradingApp(App):

```
def build(self):

    d=Dashboard()
    Clock.schedule_interval(d.update,5)

    return d
```

TradingApp().run()
