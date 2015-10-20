from suds.client import Client

hwProvider1 = 'http://ec2-52-68-193-33.ap-northeast-1.compute.amazonaws.com:8080/WeatherHistoryProvider?wsdl'

weatherGenerator1 = 'http://ec2-52-68-193-33.ap-northeast-1.compute.amazonaws.com:8080/WeatherGenerator?wsdl'
                                          
hwClient = Client(hwProvider1)
print(hwClient)

wgClient = Client(weatherGenerator1)
print(wgClient)