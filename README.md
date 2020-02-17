# WHACK List IPS Sensor Plugin v0.1.1 

White+Black (WHACK) List is a Snort IDS Plugin, the main function of the plugin is to provide Snort with a more dynamic list of blocked IPs; using IDS devices found on the network, or found on endpoint through the internet, it is possible to update a publicily accessible WHACK list based on malicious IPs flagged by existing IDS devices.<br>Not all IDS devices have sound snort rules, many malicious IPs may bypass IDS rules,while the same malicious IP may not on another IDS, with different rules; this tool gives  

![Snort IDS](https://snort.org) + [ipset-blacklist](https://github.com/trick77/ipset-blacklist) + Some Coding. 

The general idea of how the program functions: 


## Staging: Alpha 
### To Be Done: 

- Sort Readme
- Fix Snort Log as bash command does not function
- Add adaptive ruling 

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

## More Information

Learn more about the theory behind this project on my [website](https://www.josefflewis.co.uk)