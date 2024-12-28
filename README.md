# STEMFIE-X-CadQuery-Edition 

[STEMFIE](https://www.stemfie.org/) is a construction kit for children, authored by [Paulo Kiefe](https://www.stemfie.org/about). The idea of the project is based on the design and 3D printing of universal components and connecting elements and the subsequent construction of own models.

For the parametric design of kit components (beams, braces ...) of various shapes and sizes [Brendon Collecutt](https://github.com/Cantareus/Stemfie_OpenSCAD/blob/main/docs/stemfie.scad.md) created a parametric library for openSCAD program. Other graphic programs and design CAD systems such as FreeCAD, Blender, and Tinkercad can also be used to design and construct models.

The **STEMFIE-X** kit uses the basic principles of the STEMFIE project with modifications for use as a platform for creating more complex structures and models using mechanical and electronic elements - motors, servos, electronic circuits and control by microcontrollers. The building kit is primarily intended for polytechnic teaching at secondary schools and the first semesters of universities in the teaching of parametric modeling, CAD systems, constructions of machines and mechanisms.

**STEMFIE-X CadQuery Edition** is reimplementation of the [STEMFIE-X OpenScad](https://github.com/pfabo/STEMFIE-X-OpenScad-Edition) library for Python on the CadQuery platform. The library consists of a set of classes, with the help of which it is possible to create and modify basic as well as derived components of the kit. When creating components, you can use all the features of the Python language as well as the advanced capabilities of the OpenCascade platform. The basic unit in the library is BU (Basic Unit, typically 10mm), which is used to define elementary components and library commands.

When creating models, it is possible to use the connection of elementary components or by combining them, it is possible to create specialized components using the Python program. The designed components can be generated as STL files and printed on a 3D printer using standard procedures. Standard M4 screws and common accessories are used as connecting components.



## STEMFIE-X Basic Components

* [Library installation](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0005_install.ipynb)
* [Basic Components](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0010_cmp_base.ipynb)
* [Beam Block](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0015_cmp_block.ipynb)
* [Brace](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0018_cmp_brace.ipynb)
* [Gears](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0017_cmp_gears.ipynb)
* [Pulley](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0019_cmp_pulley.ipynb)
* [Component Joints](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0024_cmp_connections.ipynb)

## STEMFIE-X Python Programming

* [Programming](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0030_programming.ipynb)
* [Operations](https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/0025_operations.ipynb)

**Notice** - the library is under development and some class names as well as their functionality may change.

<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/demo_01.png" width="600px"> 

## Update 241228

New parametric wheels in ./lib/pulley.py library

<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/demo/wheels.png" width="600px"> 

## Update 241223

New components in the library - Beam_U_Block() and Beam_H_Block().

<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/comp_1.png" width="200px"> 
<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/comp_2.png" width="200px"> 
<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/comp_3.png" width="200px"> 

## Update 241222

A small hand-powered windmill for the youngest constructors

<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/simple_windmill.jpg" width="300px">


## Examples

<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/car_01.png" width="600px"> 
<img src ="https://github.com/pfabo/STEMFIE-X-CadQuery-Edition/blob/main/img/crane.jpg" width="600px">

