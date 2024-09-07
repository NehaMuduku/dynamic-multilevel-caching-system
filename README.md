 ## Dynamic Multilevel Caching System

## Overview

This repository contains a dynamic multilevel caching system that supports multiple cache levels, various eviction policies (LRU, LFU), and dynamic cache level management.

## Code Structure

- `src/cache_level.py`: Contains the `CacheLevel` class with LRU and LFU eviction policies.
- `src/cache_system.py`: Contains the `MultiLevelCache` class that manages multiple cache levels.
- `src/main.py`: Demonstrates usage of the caching system with sample test cases.
- `tests/test_cache_system.py`: Contains unit tests for the caching system.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd dynamic-multilevel-caching-system
    ```

2. Install dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python src/main.py
    ```

4. Run tests:
    ```bash
    python -m unittest discover -s tests
    ```

## Key Decisions

- Implemented LRU and LFU eviction policies using built-in Python data structures.
- Used threading locks for thread safety.
- Allowed dynamic addition and removal of cache levels.

## Assumptions

- All caches are in-memory and there is no persistent storage.
- Eviction policies are consistent across all levels.

