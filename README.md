# dvc-NLP-simple-usecase
DVC NLP project

## Reference repository:
* [official reference repo](https://github.com/iterative/example-get-started)

* [DVC STUDIO](https://studio.iterative.ai/)

* [MY View](https://studio.iterative.ai/user/c17hawke/views/DVC-NLP-Simple-usecase-3xolnsi26a)

* [Bag of Words- Krish Naik](https://youtu.be/D2V1okCEsiE)

* [TF-IDF- Krish Naik](https://youtu.be/D2V1okCEsiE)


## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### One shot create and activate environment
```bash
conda create --prefix ./env python=3.7 -y && source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05- initialize the dvc project
```bash
dvc init
```

### STEP 06- commit and push the changes to the remote repository


### extra commands - 

```bash
echo "*.log" >> logs/.gitignore
```

```bash
git rm --cached logs/running_logs.log
```

updated by rohan 