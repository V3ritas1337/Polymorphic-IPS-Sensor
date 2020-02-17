# WHACK List IPS Sensor Plugin v0.1.1 

White+Black (WHACK) List is a Snort IDS Plugin, the main function of the plugin is to provide Snort with a more dynamic list of blocked IPs; using IDS devices found on the network, or found on endpoint through the internet, it is possible to update a publicily accessible WHACK list based on malicious IPs flagged by existing IDS devices.<br>Not all IDS devices have sound snort rules, many malicious IPs may bypass IDS rules,while the same malicious IP may not on another IDS, with different rules; this tool gives  

![snort][https://popravak.files.wordpress.com/2018/08/thumb-snort.jpg] + [ipset-blacklist](https://github.com/trick77/ipset-blacklist) + Some Coding. 

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
  - libs:
    - datetime
- Snort IDS 
- Community blacklist generated using the following shell script: 
  - [ipset-blacklist](https://github.com/trick77/ipset-blacklist)
- Linux OS (Preferebly)
- Docker Engine 
- Nginx Server (In this case, Nginx container was used for testing purposes)

```
Give examples
```

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

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
