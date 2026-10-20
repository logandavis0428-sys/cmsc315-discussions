# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

For this assignment, I created a basic legal case management program using Python. I chose this example because it relates to my experience reviewing solar contracts, organizing client documents, and tracking the progress of legal matters. The program demonstrated inheritance, class and instance namespaces, shallow copying, deep copying, and object-oriented design.

## Classes and Objects

I created a parent class named `ParentClass` to represent a general legal matter. It contained a class variable, a constructor, two instance variables, and a method for displaying case information.

I then created `ChildClass`, which inherited from `ParentClass` and represented a solar contract dispute. It added information about the solar provider, case status, and supporting documents. I used `super().__init__()` to initialize inherited attributes and overrode `display_info()` to show additional details.

## Namespaces

I created two separate child objects to demonstrate class and instance namespaces. I accessed a shared class variable through both the class and an object, then added a priority attribute to only one object. I used `__dict__` to examine the objects' individual attributes and the class namespace.

## Shallow and Deep Copying

I created an object containing a dictionary of document lists and used `copy()` and `deepcopy()` to create two copies.

After modifying the original object's contract list, the shallow copy reflected the change because it shared the nested data. The deep copy remained unchanged because its nested data was independent.

## Student-Created Extension

I added an `add_document()` method to track contracts and billing statements. The method checked for valid document categories and rejected empty document names. I chose this feature because document organization is an important part of legal case management.

## Testing

I tested the program by creating parent and child objects, displaying their information, adding documents, testing invalid input, inspecting namespaces, and comparing shallow and deep copies.

## Discussion Board Reflection

This assignment helped me understand how inheritance, namespaces, and object copying work together in Python. I had previously understood classes as a way to organize code, but this exercise showed me how they can represent information that changes from one object to another. I found inheritance particularly useful because the child class could reuse basic client information while adding details specific to solar contract disputes.

The most challenging part was understanding shallow and deep copying. Initially, I assumed that copying an object would make all its information independent. After modifying a nested document list, I could see why that assumption was incorrect.

Compared with procedural programming, which organizes a program around functions and steps, object-oriented programming groups related data and behaviors into objects. This approach required more planning, but it made the program easier to understand.

I also saw how inheritance and reusable methods could improve maintainability. If I needed to update how basic case information was displayed, I could make that change in the parent class rather than rewriting the same code for every case type.
