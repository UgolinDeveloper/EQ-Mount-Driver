# EQ Mount Driver

## Why this project ?

<div align="justify">
The observation of the starry sky is often done at night, it is better. However
I like to sleep at that time ...

Astrophotography consists in taking pictures through a telescope with exposure times of several hours. Whether it is for take a picture of a nebula, to record the movement of an asteroid or to measure the orbits of the satellites of Jupiter. With all the technology readily available today, why deprive yourself of automating all this?

So the first step is to be able to take control of the telescope mount remotely. What's better than an accessible web server
with any browser on which I could view the orientation
of the telescope and give it the order to orient itself according to the specific coordinates of a celestial body?

</div>

</p>

<img src='src\img\Stars.jpg' alt=Stars style="border-radius:5%">

## Stepper motors

<div align="justify">
Stepper motors are motors that specialize in the precise angular positioning of their output shafts. They are controlled in a loop
open, i.e. we make the material conance so that it really turns as we ask it to. No need to control the nodal orientation.
</div>

<p align="center">
    <img src='src\img\Stepper motor.png' width=200px alt='Stepper Motor' style="border-radius:5%">
</p>

## Synoptic

For the project, physically the stepper motors will be driven via a dedicated raspbery shield:

<img src='src\img\Schema.PNG' alt=Schema style="border-radius:5%">

## Code

- [x] [launcher](https://github.com/UgolinDeveloper/Project-2/blob/master/launcher.py)
- [x] [.gitignore](https://github.com/UgolinDeveloper/Project-2/blob/master/.gitignore)
- [x] [src](https://github.com/UgolinDeveloper/EQ-Mount-Driver/tree/master/src)
  - [x] [main](https://github.com/UgolinDeveloper/EQ-Mount-Driver/blob/master/src/main.py)
  - [x] [img](https://github.com/UgolinDeveloper/EQ-Mount-Driver/tree/master/src/img)
