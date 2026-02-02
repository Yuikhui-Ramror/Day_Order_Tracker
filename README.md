# Day Order Tracking System

This is a small project built to solve a real problem faced in colleges that follow a **day-order based timetable** instead of fixed weekdays.

In such systems, holidays often shift the day order, and students end up manually calculating whether today is Day 2, Day 3, etc. This project automates that process and acts as a single source of truth.

---

## Why This Project?

In my college, the timetable follows a rotating day order system (Day 1 – Day N).  
Whenever an unexpected holiday occurs:

- Day orders shift
- Students get confused
- Everyone depends on classmates to confirm the timetable
- Classes are sometimes missed

There was no simple system that could just tell:
> “What is today’s day order and what classes do I have?”

This project is my attempt to solve that.

---

## What This System Does

- Calculates the correct day order automatically
- Skips holidays and non-working days
- Resets the day order after completing the cycle
- Keeps logic, data, and UI separate
- Provides a basic admin portal to manage holidays

The focus is on **correct logic first**, not heavy UI or extra features.

---

## Features

- Day order calculation (Day 1 to Day N)
- Holiday handling
- Support for working / non-working days
- Simple admin portal to update holidays
- Student view to check today’s schedule
- Clean and modular project structure
---
