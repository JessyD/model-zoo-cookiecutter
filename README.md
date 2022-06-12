# model-zoo-cookiecutter

## How to use it?
**1. Install Cookiecutter:**

```
pip install -U cookiecutter
```
or 
```
conda config --add channels conda-forge
conda install cookiecutter
```

**2. Run cookiecutter to create the template:**
```
cookiecutter template
```

**3.Enter your model's information:** 
You will be asked for the following information:
```
"example_name": "example_name",
"author_name": "Your name (or your organization/team)",
"description": "A short description of the example.",
"dataset_path": "The local path to the dataset being used"
```

**4. This will create the following directory tree:**
```
{example_name}
├── README.md
├── data
├── model
│   └── model-{example_name}_smdl.json
    └── {example_name}.ipynb
```

