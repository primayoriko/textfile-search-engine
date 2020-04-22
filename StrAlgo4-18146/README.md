# Simple Search Engine 
## Description
------------
Simple Web-based News Search Engine from Text File using Booyer-Moore, KMP algorithm and RegEx with Flask Server.

## Requirements
-----------
1. *Python 3*, here I'm using python 3.7
2. Recommended using *Windows*, as I'm using it. But, you can try in linux, such as Ubuntu Linux
3. Latest Web Browser, recommended using *Google Chrome* or *Mozilla Firefox* as I've tested this web apps work on them.
4. *Virtualenv* (a python lib, for creating virtual/special environment to a specific project)
5. Additional python lib/framework: *flask*, *python-dotenv* (of course all of it installed in venv)
   
You can install virtualenv by executing **install_venv.bat**, and when inside virtuelenv, you can executing **install_library.bat** to install additional python library needed for this web application.

## How to Run
------------
1. Make sure you've install all requirements above. If you don't, please follow step that I've mentioned above (for some requirements) before you proceed to the next step.
2. open shell (cmd/powershell) and change directory to **env/Script**.
3. Execute
    
            activate
    to run virtualenv.
4. Execute
      
        flask run
   to run the server.

For simplicity you can executing **start_env.bat** instead of step 2-3 to running virtualenv for simplicity.

## How to Use
--------
1. After you run the server by *flask run*, you can navigate to 
   
        http://127.0.0.1:5000/
   or

        localhost:5000/

   with your web browser to run this web apps. 
2. Choose your text file, enter keyword, select algorithm you want, and then click **Search!** button.
3. Then the result must appear after awhile.
4. Enjoy.

## Notes
-----------
1.  There is still some bug for *Jumlah* and *Waktu* information because of regex used still limited. You can try to improve this by editing Regex in Matcher class in the **src/matcher.py** file.