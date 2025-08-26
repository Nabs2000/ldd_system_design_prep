# 🚗 **Ride Sharing System**

## 📌 Problem Statement

You are designing a simplified **Ride Sharing System** (think Uber/Lyft, but much smaller in scope).

The system should support:

* **Drivers**: Each driver has an ID, name, car type (`"SEDAN"`, `"SUV"`, etc.), and availability status (`AVAILABLE` / `BUSY`).
* **Riders**: Each rider has an ID, name, and location.
* **Rides**: A ride links one driver and one rider.

## Rules

1. Only **available drivers** can be matched to a ride.
2. If multiple drivers are available, pick **the first one you find** (no fancy nearest-driver logic needed).
3. A driver can only have **one ride at a time**.
4. When a ride ends, the driver becomes available again.

## Tasks

Implement a system with the following methods:

1. `request_ride(rider)` → Assigns an available driver to the rider and creates a ride.
2. `end_ride(ride)` → Ends the ride and marks the driver as available.
