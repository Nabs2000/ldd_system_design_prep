# 🐶 Dog Park Management System

## 📌 Problem Statement

You are building a system to manage a **Dog Park Business**.

There are two types of playgrounds:

1. **Small Dog Playground** – only accepts small dogs and has a smaller capacity.
2. **Large Dog Playground** – only accepts large dogs and has a larger capacity.

### Rules

* Only **vaccinated dogs** can enter.
* Dogs **older than 10 years** are not allowed.
* In the future, playgrounds may also reject **dogs that shed skin**, so the system should be easy to extend.

Your job is to implement the following functionality:

1. **check\_in(dog)** → Assigns a dog to the appropriate playground if possible.
2. **check\_out(dog)** → Removes a dog from the playground.
