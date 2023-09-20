
# Phone Number Location Tracker using Python


Are you curious about the location of a mobile number? Maybe you want to track a lost phone...

Track a mobile number's location using Python.



## Installation

I am using phonenumbers module in this project

```bash
  pip install phonenumbers
```
Importing necessary modules-:

```bash
  import phonenumbers
  from phonenumbers import timezone,geocoder,carrier
```
## Usage/Examples
Here is a sample code to use phonenumbers module
```javascript
phone_number=phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone_number)
service_provider = carrier.name_for_number(phone_number, "en")
sim_region = geocoder.description_for_number(phone_number, "en")
}
```

##### Enter a mobile number with country code-:
      e.g., +9193062.....


## Output

``` 
Country Code: 91 National Number: 93062.....
Time zone : ('Asia/Calcutta',)
Sim card provide : Reliance Jio
Sim region : India
```
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/DharmenderKaushik)


