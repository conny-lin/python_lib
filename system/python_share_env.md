# Share python environment set up
Created by: Conny Lin | July 2020


## Create an environment for the project (using conda)
Note you will need to have conda installed. This will not apply if you do not use conda.

1. Create a separate environment for the project using `conda create`. For example,
    `conda create -n viper`
    
    Note: use `conda info --envs` to check your current environments.

2. Activate the environment. For example, `conda activate viper`

3. Install python packages in the project's environment. For example, `conda install jupyter pandas numpy`. Note that packages you installed in your base environment won't appear in the new environment. You'll need to install them again. Try to install only the packages this project will need.

4. If you'd like add the enviroment to jupyter notebook, you'd need to add the environment as a kernel. For example, `ipython kernel install --name "viper" --user`


## Sharing environments
To share the enviroment you used for this project, export the environment information. For example, `conda list --explicit > viper_env.txt`

Create a new environment using the `viper_env.txt` file. For example, `conda create -n viper_new_env --file viper_env.txt`


## Remove an environment
To remove an environment, we can use the following command: `conda remove --name myenv --all`

Be careful with this command, as you can't get an environment back!

We can check if we still have the environment: `conda info --envs`




