# Operating Systems Algorithms (CSC 314)

This repository contains implementations of various operating system algorithms, covering process scheduling, memory management, and synchronization. The code is intended to demonstrate the practical application of concepts learned in the CSC 314 Operating Systems course using Python.

## Project Structure

The repository is organized by algorithm type. Each directory contains the source code and relevant documentation for that specific implementation.

## Implementation Status

Below is the current status of the algorithms in this repository.

### CPU Scheduling(Disk Scheduling)
- [x]  Shortest Job Next(SJN)
- [ ] Shortest Remaining Time (SRT) - *Under Development*
- [ ] Round Robin
- [ ] Multi-level Queues
- [x]  First Come First Serve (FCFS)
- [x] Priority Scheduling

### Memory Management
- [ ] Next Fit - *Under Development*
- [x] Worst Fit
- [x] First Fit
- [x] Best Fit

### Page Replacement Policies
- [x] FIFO (First-In, First-Out)
- [x] LRU (Least Recently Used)
- [x] Optimal Page Replacement

*(Note: Checkboxes marked with [x] represent fully implemented algorithms. Unmarked boxes indicate algorithms that are currently being implemented or optimized.)*

## Development Status

**Active Development:** This repository is a work in progress. Additional algorithms, optimizations, and documentation are actively being implemented and will be pushed to the repository in upcoming updates as the course curriculum advances.

## Getting Started

To test these implementations on your local machine, follow the steps below.

### Prerequisites
* Python 3.x

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/ojayballer/OPERATING-SYSTEMS-CSC-314-.git](https://github.com/ojayballer/OPERATING-SYSTEMS-CSC-314-.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd OPERATING-SYSTEMS-CSC-314-
    ```

### Usage
Navigate to the specific algorithm folder you wish to test. For example:

```bash
cd CPU_Scheduling/FCFS
python main.py
