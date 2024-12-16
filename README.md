# EPAiV5-Session23
Session - 23: Descriptors

# Python Descriptrs Assignment
![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session23/actions/workflows/python-app.yml/badge.svg)

# UserProfileManager System

A Python implementation of a user profile management system utilizing descriptors for attribute validation and caching.

## Overview

This project demonstrates advanced Python concepts including:
- Custom descriptors for property validation
- Weak reference caching mechanisms
- Property resolution and overrides

## Features

### 1. Validated Properties
- Username validation (non-empty string)
- Email validation (must contain "@" and ".")
- Last login tracking (datetime object, nullable)

### 2. Caching System
- Implements caching for recently used profiles
- Uses weak references to prevent memory leaks
- Automatic cache cleanup when references are no longer used

### 3. Property Management
- Custom descriptor implementation for property validation
- Automatic name binding using `__set_name__`
- Proper memory management