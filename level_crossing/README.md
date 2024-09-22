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

