# Keeping Behavioral Programs Alive: Specifying and Executing Liveness Requirements

This repository contains all code for the following evaluations presented in the paper:

## Level Crossing
**Note: the project was implemented and tested on Python 3.9.16**

### Installation 

Set a virtual environment to run the code:
```shell
cd level_crossing
python -m venv env 
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Usage

To run a DFS and get the state space, use the `main_dfs_single.py`:
```shell
python main_dfs_single.py --n 50 --k 1 --m 1
```

To run the DRL algorithm and get the time that takes the algorithm to reach a policy, use the `main_mask.py`:
```shell
python main_mask.py --n 50 --k 1 --m 1 --total_timesteps 100000 --repeat 5
```

## Sokoban

**Note: the project requires Conda**


### Installation



Create a virtual environment and activate it:

```shell
cd sokoban
conda create --name bp-sokoban python=3.7 --file requirements.txt
conda activate bp-sokoban
```


### Usage
*IMPORTANT: The evaluation requires a lot of RAM.
We recommend using a machine with at least 64GB of RAM.*

#### Run parameters:
* map name - the name of the map to run on. one of the following:
    * map_6_8_3
    * map_12_11_1
    * map_13_12_1
    * map_9_10_2
    * map_7_7_2
    * map_7_7_3
    * map_11_9_2
    * map_6_6_3
    * map_6_7_3
    * map_8_8_2
    * map_8_2
    * map_10_9_2
    * map_9_7_2_
    * map_9_7_2
    * map_10_7_2
    * map_8_9_2
    * map_8_7_2
    * map_9_8_2
    * map_9_9_2
    * map_11_8_2
* single/multiple requirements - whether to run the single ("0") or multiple ("1") liveness requirements scenario.

#### Executing the code
An example of running the code on the map_6_8_3 map with the single liveness requirement scenario is as follows:
```shell
python main_sokoban.py "map_6_8_3" "0"
```


## Dwyer Patterns
**Note: the project was implemented and tested on Python 3.9.16**

### Installation 

Set a virtual environment to run the code:
```shell
cd dwyer_patterns
python -m venv env 
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Usage

To run a check of a single pattern run the `check.py`:
```shell
python check.py --pattern 8
```



