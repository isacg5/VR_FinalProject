# Final Project of Virtual Reality for Robotics
## Group Members | Name-Surname & GitHub Account
* Chloé Bohler | [@Naochloe2](https://github.com/Naochloe2)
* Baris Aker | [@barisakerr](https://github.com/barisakerr)
* Abdelouadoud Guelmami | [@wadoud01](https://github.com/wadoud01)
* Isabel Cebollada Gracia | [@isacg5](https://github.com/isacg5)

## Introduction
Our project focuses on the simulation of the deployment of a medical aerial drone alongside an ambulance
within the streets of Genova, Italy. Our focus is on seamlessly integrating the drone’s movement with the am-
bulance’s route, navigating through the bustling urban environment to reach remote mountainous areas where
traditional vehicles may struggle to access due to external consitions such as environmental factors. By leveraging the capabilities of Unreal Engine, we aim to create a
realistic and immersive experience that not only showcases the technical prowess of game development but also
highlights the potential impact of such technology on real-world scenarios

## Tools used
For the execution of the project it is necessary to have installed the following tools on Windows 10
* [Colloseum](https://github.com/CodexLabsLLC/Colosseum): It is a simulator for robotic, autonomous systems, specifically drone testing, built on Unreal Engine. Is
open-source and cross platform, and is a fork of AirSim, that Microsoft shutdown on 2022 and allows
maintenance and support for newer versions of Unreal Engine. It provides a high quality simulation
environment that simulates with high fidelity all the dynamics of aerial vehicles.
* Python 3.12.1: Is a high level object oriented programming language that allows to create codes for different
purposes.
* Unreal Engine v. 5.2.1: It is a video game development tool from the video game and software development company Epic Games.
With this tool, developers have the ability to build a simulation, edit videos or sound, and render anima-
tions. There is also necessary to have installed the next plugins:
  * Cesium for unreal plugin: It provides a high accuracy 3D geospatial ecosystem to Unreal Engine. By using Google Maps API, it
provides with 3D Tiles and cloud-based real-world content from Cesium ion to Unreal Engine.
  * TCP Sockets plugin: It is a software structure that allows communication through the network between a client and a server
 
Other tools that have been used for the development of the proeject:
* Visual Studio v.2022: It is an IDE for creating applications on Windows, Android or IOS among others.
* D-flight website: This tools allows to have knowledge about the aerial restrictions for the drones, such as restricted zones
or restricted heights to flight.

## How to run it?
*Clone the repository:
```console
git clone https://github.com/isacg5/VR_FinalProject.git
```
*Make sure you put settings.json under Airsim folder of your installation
*Run the script for the drone:
```console
python ./script.py
```
* Get Unreal Engine project [here](https://www.google.com) (you will need permissions from the owner)
* Run Unreal Engine project
  
## Possible improvements
Possible improvement for this project could be to include a planner algorithm according to the limitations of the map and the desired goal, not only by counting with the places provided by the dataset. In this way, there would be a more effective navigation to some places not taken into account before.

## Video 
<p align="justify">
  Below you can find a video that shows the whole behavior of the poject
</p>

[![Watch the video](https://github.com/isacg5/VR_FinalProject/blob/main/resources/pic.png)](https://youtu.be/fnaDAoXy14A)


