This is my final project for DSCI 6672 - Cybersecurity with Machine Learning.

The original Gym-Malware which was created with the purpose of comparing RL algorithms for modifying malware to evade 
a Malware Classifier.

Gym-Malware can be found here: https://github.com/endgameinc/gym-malware

Malware Aquisition can be done from theZoo repository found here: https://github.com/ytisf/theZoo


Any files outside of the gym-malware-master folder are supplementary files from the results for my final presentation. 
The repository is meant to be used inside of Google Collab and is altered to be able to zip the project for discontinuous
training intervals in regards to Google Collab's runtime disconnection.

Outside of the gym-malware-master folder should be:
1. Presentation slides
2. Two generated textfiles of results from my experimentation with the Boltzmann Q Policy. One contains the statistic summary of the dataset results. The other provides the name (sha256) of the samples, along with the action(s), that successfully evaded the Malware Classifier.
3. Two other generated textfiles of the same name but indicated with (1), results with the model policy set EpsGreedyPolicy and evaluation policy to best_action which is the argmax of the Q-values. Note: this is set for testing, the model was still trained on Boltzmann Q Policy.
4. ransom_list.txt provides the associated name and sha256 of the Ransomware taken from the Zoo.
5. misclassified.txt contains all of the original sha256 name associations are misclassified by the Gradient Boosting Tree Malware Classifier.

The general framework is kept from gym-malware; however, I'd like to note a few important differences:
1. The RL alogorithm implemented is only Double DQL, the baseline model is random.
2. Requirement.txt has some updated packages to avoid breaking runtime.
3. Most of the altercation revolved around interval saving the policy, weights, history, and memory.

Some absolutes before running the code:
1. Edit train_agent_kerasrl.py for the desired destination/Google Drive destination
2. Edit Malware_Env.py if you would like a different test_train_split percentage (.2)
3. Edit test_agent_kerasrl.py and set current_set to sha256_holdout, sha256_full, or sha256_train for
desired set to test on. It was left with sha256_full.
4. Once generated files in savepoint, if you would like to delete all previously saved files, delete them and rename the
current file in each folder with the padded value of 000. The code added relies on the latest file update to be the last
file when sorted; otherwise will not sort correctly.

Once you read all of that: One can fork a copy of jupyternotebook to get it started.

Jypter Notebook: 
https://drive.google.com/open?id=1I-dXUroohAwgfmHiJq03ylLvC-DHnu8N

The notebook downloads the .zip so that my entire repository isn't forked. The unzipped folder is just the general things you'll find in the zip, except the init files.





Youtube video link of introduction and instructions: to be posted.
