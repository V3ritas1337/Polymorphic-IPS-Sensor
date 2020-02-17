# WHACK List IPS Sensor Plugin v0.1.1 

The main function of the plugin is to provide Snort with a more dynamic list of blocked IPs using IDS devices found on the network or found on endpoints through the internet. As IDS system rules have to be manually updated or through vendor updates, it is not an efficient way to keep up with the amount of malicious packets found through the internet. The WHACK list will update existing blacklists that Snort will use, therefore preventing attacks opposed to detecting attacks. 

*Defence in Depth*
Furthermore, as rules are not always an effective method (plethora of reasons.. not updated, new signatures etc.), a blocked attack on one network may not be blocked on another. This is a solution as the potentially vulnerable network will have an updated blacklist, so it may not be totally necessary to use rules as main defence method.

It is possible to update a publicily accessible WHACK list based on malicious IPs flagged by existing IDS devices.<br>

[Snort IDS](https://snort.org) + [ipset-blacklist](https://github.com/trick77/ipset-blacklist) + Some Python Coding. 

## How the program functions: 

![Flow Chart](https://github.com/V3ritas1337/Polymorphic-IPS-Sensor/blob/master/images/flowChartFinal.svg)


- **Cron: Has One Hour Passed?**:  This cron job is used to execute the core.py script. 

- **blacklist.sh**: It will check through open source community blacklists for new entries, adding to the existing blacklist. At the same time using *core.py* more IPs will be added based on alerts. 

- **core.py**: This script checks for alerts from Snort. 

  - **Are there Alerts?**: If yes, it will check in the alerts for the word "spp_reputation", this word is associated with blacklisted IPs. 

  - **Split Alert Line into Array**: This is to locate the malicious IPs in the alert file, where it will append the local blacklist from ipset-blacklist.   

  - **Open and Append Existing Blacklist**: From the ipset-blacklist, it will append it with found malcious IPs from snort. This is where Detection can become Prevention.  

**update-blacklist.sh**: once all this has been done, the blacklist will be uploaded to a web server which can be downloaded and / or updated from other IDS systems running this program.  


## Staging: Alpha 
### To Be Done: 

- Sort Readme
- Fix Snort Log as bash command does not function
- Add adaptive ruling 
- Authentication is needed for website as anyone can upload to central server (potential single point of failure
  
## Getting Started

<b>You are going to want some gifs of the program working<b> 
<b>Image of basic idea of the program<b>

### Prerequisites

- Python v3.4+
- Snort IDS 
- Community blacklist generated using the following shell script: 
  - [ipset-blacklist](https://github.com/trick77/ipset-blacklist)
- Linux OS (Preferebly)
- Docker Engine 
- Nginx Server (In this case, Nginx container was used for testing purposes)

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Snort IDS](https://www.snort.org/) - The Intrusion Detection System used. 
* [Nginx](https://www.nginx.com/) - Web Server used. 
* [IPSet-Blacklist](https://github.com/trick77/ipset-blacklist) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. 

## Authors

* **Joseff Lewis** - *Initial work* - [Website for More Information](https://josefflewis.co.uk)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Derrick Newton - Coventry University: mentor for the duration of this ongoing project.  
* User Trick77 - Awesome Open Source Blacklists. 
<<<<<<< Updated upstream

## More Information

Learn more about the theory behind this project on my [website](https://www.josefflewis.co.uk)
=======
>>>>>>> Stashed changes
