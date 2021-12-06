# pip install virtualenv

# virtualenv myproject123  // creates a new env

# source myproject123/bom/activate 
# Windows: myproject123\Scripts\activate.ps1

# now stuff will be installed in another environment


# deactivate  //deactivates the virtual env

# in case when you want to install, update any framework and the future ones doesnt work with your old projects
# thus, virtual env comes in clutch

# pip freeze        // returns all installed packages
# pip freeze > requirements.txt

# in virtual env,
# pip install -r .\requirements.txt   //installs all packages in virtualenv

