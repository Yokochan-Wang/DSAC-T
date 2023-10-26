## Reference
- [Distributional Soft Actor-Critic (DSAC)](https://arxiv.org/abs/2001.02811)
- [Distributional Soft Actor-Critic with Three Refinements (DSAC-T)](https://arxiv.org/abs/2310.05858)


## Requires
1. Windows 7 or greater or Linux.
2. Python 3.8.
3. The installation path must be in English.


## Installation
```bash
# Please make sure not to include Chinese characters in the installation path, as it may result in a failed execution.
# clone DSAC2.0 repository
git clone git@github.com:Jingliang-Duan/Distributional-Soft-Actor-Critic-2.0.git
cd Distributional-Soft-Actor-Critic-2.0
# create conda environment
conda env create -f DSAC2.0_environment.yml
conda activate DSAC2.0
# install DSAC2.0
pip install -e.
```


## Train
These are two examples of running DSAC2.0 on two environments. 
Train the policy by running:
```bash
cd example_train
#Train a pendulum task
python main.py
#Train a humanoid task. To execute this file, Mujoco and Mujoco-py need to be installed first. 
python dsac_mlp_humanoidconti_offserial.py
```
After training, the results will be stored in the "Distributional-Soft-Actor-Critic-2.0/results" folder.

## Simulation 
In the "Distributional-Soft-Actor-Critic-2.0/results" folder, pick the path to the folder where the policy will be applied to the simulation and select the appropriate PKL file for the simulation.
```bash
python run_policy.py
#you may need to "pip install imageio-ffmpeg" before running this file on Windows. 
```
After running, the simulation vedio and state&action curve figures will be stored in the "Distributional-Soft-Actor-Critic-2.0/figures" folder.


## Acknowledgment
We would like to thank all members in Intelligent Driving Laboratory (iDLab), School of Vehicle and Mobility, Tsinghua University for making excellent contributions and providing helpful advices for DSAC 2.0.
